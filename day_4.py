# loop detection using a set
def is_looping(n):
    def next(num):
        nxt = 0
        while num>0:
            curr=num%10
            nxt+=curr**2
            num//=10
        return nxt
    visited = set()
    while n!=1:
        if n in visited:
            return True
        visited.add(n)
        n=next(n)
        return False
        