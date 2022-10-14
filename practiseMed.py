# med practise question with loops 

print("=====================================")

# 1. Given a string and a non-negative int n, return a larger string that is n copies of the original string.


#string_times('Hi', 2) → 'HiHi'
#string_times('Hi', 3) → 'HiHiHi'
#string_times('Hi', 1) → 'Hi'

def string_times(str, n):
  result = ""
  for _ in range(n):
   result += str
  return result 

print(string_times("hello", 4))

print("=====================================")

# 2. Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;


#front_times('Chocolate', 2) → 'ChoCho'
#front_times('Chocolate', 3) → 'ChoChoCho'
#front_times('Abc', 3) → 'AbcAbcAbc'

def front_times(str, n):
  front = str[:3]
  answer=""
  for i in range(n):
    answer += front
  return answer 

print(front_times("meow", 3))

print("=====================================")


#3. Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".


#string_bits('Hello') → 'Hlo'
#string_bits('Hi') → 'H'
#string_bits('Heeololeo') → 'Hello'

def string_bits(str):
  answer = ""
  for i in range(len(str)):
    if i % 2 == 0:
      answer += str[i]
  return answer

print(string_bits("froggy"))

print("=====================================")


#4. Given a non-empty string like "Code" return a string like "CCoCodCode".


#string_splosion('Code') → 'CCoCodCode'
#string_splosion('abc') → 'aababc'
#string_splosion('ab') → 'aab

def string_splosion(str):
  answer = ""
  for i in range(len(str)):
    answer += str[:i+1]
  return answer

print(string_splosion("meow"))

print("=====================================")

#5 

#6 Given an array of ints, return the number of 9's in the array.


# array_count9([1, 2, 9]) → 1
# array_count9([1, 9, 9]) → 2
# array_count9([1, 9, 9, 3, 9]) → 3

def array_count9(nums):
  count = nums.count(9)
  return count 

print(array_count9([1, 9, 9, 5]))

print("=====================================")

