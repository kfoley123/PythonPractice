# med practise question with loops 
# https://codingbat.com/prob/p145834

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

#5 Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).


# last2('hixxhi') → 1
# last2('xaxxaxaxx') → 1
# last2('axxxaaxx') → 2



#6 Given an array of ints, return the number of 9's in the array.


# array_count9([1, 2, 9]) → 1
# array_count9([1, 9, 9]) → 2
# array_count9([1, 9, 9, 3, 9]) → 3

def array_count9(nums):
  count = nums.count(9)
  return count 

print(array_count9([1, 9, 9, 5]))

print("=====================================")

#7 Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.


# array_front9([1, 2, 9, 3, 4]) → True
# array_front9([1, 2, 3, 4, 9]) → False
# array_front9([1, 2, 3, 4, 5]) → False

def array_front9(nums):
  for count, value in enumerate(nums):
    
    if count <= 3 and value == 9:
      return True
   
  return False 

  print(array_front9([1,2,7,5,9]))

  print("=====================================")

#8 Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.


# array123([1, 1, 2, 3, 1]) → True
# array123([1, 1, 2, 4, 1]) → False
# array123([1, 1, 2, 1, 2, 3]) → True

def array123(nums):
  for i in range(len(nums) -2):
    if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
      return True
  return False 

  #https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/

  #1 Print First 10 natural numbers using while loop
# expected output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

i = 0 
while i <= 9:
	i += 1
	print(i)

  #2 Print the following pattern

# expected output:
# 1
# 1 2
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 

i = 1
for x in range(5):
	print("loop", x)
	i+=1
	for y in range(1,i):
		print(y)

print("=====================================")

#3 Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number

# For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)

def numberSum(num):
    total = sum(range(1, num))
    print(total)
        
(numberSum(10))

print("=====================================")

#4 Write a program to print multiplication table of a given number
#For example, num = 2 so the output should be
#2
#4
#6 
#8 
#10
#12
#14
#16
#18
#20

def numMultiply(num):
    for x in range(10):
        x += 1 
        print(x*num)

numMultiply(5)


print("=====================================")


#5 Write a program to display only those numbers from a list that satisfy the following conditions

# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the next number
# If the number is greater than 500, then stop the loop

# given numbers= [12, 75, 150, 145, 525, 50]
# output: 75 150 145 

def numFilter(nums):
    answer = []
    for x in nums:
        if x > 500:
           break
        elif x > 150: 
            continue
        elif x% 5 == 0:
            print(x)


numFilter([12, 75, 150, 180, 145, 525, 50])

print("=====================================")

#6 Write a program to count the total number of digits in a number using a while loop.

def digitCount(num):
    count = 0 
    answer = map(int, str(num))
    for x in answer:
        count += 1
    print(count)

digitCount(21342646)

print("=====================================")


#7 Write a program to use for loop to print the following reverse number pattern

# 5 4 3 2 1
# 4 3 2 1
# 3 2 1 
# 2 1
# 1

i = 1 
for x in range(5):
    print("loop", x)
    i += 1
    for y in range(7 -i, 0, -1):
        print(y) 

print("=====================================")

#8 Print list in reverse order using a loop

def reverseList(nums):
    i = len(nums)
    for x in nums:
        i -= 1
        print(nums[i])

reverseList([10, 20, 30, 40, 50])

print("=====================================")

#9 Display numbers from -10 to -1 using for loop

#expected output -10 -9 -8 -7 -6 -5 -4 -3 -2 -1

for num in range(-10, 0, 1):
    print(num)

print("=====================================")

#10 Use else block to display a message “Done” after successful execution of for loop

for i in range(5):
    print(i)
else:
    print("done!")