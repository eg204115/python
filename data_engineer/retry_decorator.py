import logging
import time
from functools import wraps          # wraps: preserves the wrapped function's __name__/docstring
from typing import Callable, TypeVar  # Callable: type for "a function"; TypeVar: generic placeholder type

logger = logging.getLogger(__name__)  # __name__ = this module's path, used so log lines show their origin
T = TypeVar("T")                      # T stands in for "whatever type the wrapped function returns"


def retry(max_attempts: int = 3, backoff_seconds: float = 2.0) -> Callable:
    """Retry a function with exponential backoff. Use for flaky I/O (APIs, DB, S3)."""
    # This outer function takes arguments (max_attempts, backoff_seconds) and
    # returns a decorator. This "decorator factory" pattern is how you make
    # a decorator itself configurable with arguments.

    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        # func: the actual function being decorated (e.g. fetch_partition)
        # Callable[..., T] means "a function taking any args, returning type T"

        @wraps(func)  # copies func's metadata onto wrapper, so debugging/introspection isn't broken
        def wrapper(*args, **kwargs) -> T:
            # *args / **kwargs: capture any positional/keyword arguments so this
            # decorator works on functions with any signature
            last_exc = None
            for attempt in range(1, max_attempts + 1):  # 1-indexed attempts for human-readable logs
                try:
                    return func(*args, **kwargs)  # call the original function, passing args through
                except Exception as exc:          # catch broadly here because we re-raise below anyway
                    last_exc = exc
                    wait = backoff_seconds * (2 ** (attempt - 1))  # exponential backoff: 2s, 4s, 8s, 16s...
                    logger.warning(
                        "Attempt %s/%s failed for %s: %s. Retrying in %.1fs",
                        attempt, max_attempts, func.__name__, exc, wait,
                    )  # %s/%.1f: lazy string formatting — logging only builds the string if it's emitted
                    time.sleep(wait)
            # "raise ... from last_exc" preserves the original traceback chain
            # instead of hiding it behind a generic RuntimeError
            raise RuntimeError(f"{func.__name__} failed after {max_attempts} attempts") from last_exc
        return wrapper
    return decorator


@retry(max_attempts=4)  # decorator syntax: fetch_partition = retry(max_attempts=4)(fetch_partition)
def fetch_partition(source_client, date_str: str) -> list[dict]:
    return source_client.get_records(partition_date=date_str)