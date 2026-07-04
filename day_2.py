def last_num(arr):
    if len(arr)==0:
        return None
    return arr[-1]
print(last_num([3,4,6]))

def max_num(arr):
    if len(arr)==0:
        return None
    max_num = arr[0]
    for num in arr:
        if max_num < num:
            max_num = num
    return max_num
print(max_num([34,67,2]))

def separate_numbers(arr):
    if len(arr)==0:
        return None
    odd = []
    even = []
    for num in arr:
        if not isinstance(num, int):
            continue
        if num%2==0:
            even.append(num)
        else:
            odd.append(num)
    return odd, even

print(separate_numbers([1,2,3,4,5,6]))
print(separate_numbers([]))
print(separate_numbers([1, -2, 3, 0]))
print(separate_numbers([1, 2, "hello", 4.5, 7]))


def reverse_array(arr):
    if len(arr)==0:
        return []
    if len(arr)==1:
        return arr
    left = 0
    right = len(arr)-1
    while left<right:
        arr[left], arr[right] = arr[right], arr[left]
        left +=1
        right-=1
    return arr


text = "banana"
count ={}
for ch in text:
    if ch in count:
        count[ch]+=1
    else:
        count[ch] =1
print(count)



def two_sum(arr, target):
    if len(arr)<2:
        return []
    seen = {}
    for num in arr:
        if not isinstance(num, (int, float)):
            continue
        complement = target - num
        if complement in seen:
            return [num, complement]
        seen[num] = True
    return []

print(two_sum([2,3,4,5,6,7], 5))

def max_pair_sum(arr):
    if len(arr)<2:
        return []
    first = second = float('-inf')
    for num in arr:
        if not isinstance(num, (int, float)):
            continue
        if num>first:
            second = first
            first=num
        elif num>second:
            second = num
    return first + second


print(max_pair_sum([1,9,3,7]))
print(max_pair_sum([1]))
print(max_pair_sum([-10,-5,-1]))
print(max_pair_sum([1,"abc",5]))



def frequency(arr):
    if len(arr)==0:
        return None
    freq = {}
    for num in arr:
        freq[num]= freq.get(num, 0)+1

    return freq

print(frequency([1,3,4,4,2,3,2,1,3,2,2,1,3,4,5,3]))

def remove_duplicates(arr):
	if len(arr) ==  0:
		return []
	seen = set()
	result = []
	for num in arr:
		if num not in seen:
			seen.add(num)
			result.append(num)
	return result

def is_palindrome(s):
    if s == "":
        return True
    s = s.lower().replace(" ","")
    return s==s[::-1]

def count_vowels(s):
    if s == "":
        return 0
    vowels = "aeiou"
    count = 0
    for ch in s.lower():
        if ch in vowels:
            count+=1
    return count

def find_min(arr):
    if len(arr)==0:
        return None
    min = arr[0]
    for num in arr:
        if not isinstance(num, (int, float)):
            continue
        if num<min:
            min = num
    return min