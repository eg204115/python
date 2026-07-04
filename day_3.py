def second_largest(arr):
    if len(arr)<2:
        return None
    first = second = float('-inf')
    for num in arr:
        if not isinstance(num,(int,float)):
            continue
        if num>first:
            second=first
            first=num
        elif second>num and first!=num:
            second = num
    if second == float('-inf'):
        return None
    return second

def is_anagram(s1,s2):
    s1 = s1.lower().replace(" ","")
    s2 = s2.lower().replace(" ","")
    if len(s1) != len(s2):
        return False
    return sorted(s1)==sorted(s2)



def pair_sum(arr, target):
    left = 0
    right = len(arr)-1
    while left < right:
        current = arr[left]+ arr[right]
        if current == target:
            return [arr[left], arr[right]]
        if current < target:
            left += 1
        else:
            right -= 1


def find_du
