# # 1. Remove All Spaces
# # Definition: A space (' ') is a blank character between words.
# # Task: Remove all spaces from the given string.
# # Example Input: Python Programming
# # Example Output: PythonProgramming
# str="Python Programming"
# removed_spaces=str.replace(" ","")
# print(removed_spaces)

# # 2. camelCase to snake_case
# # Definition: camelCase uses capitals after first word; snake_case uses underscores.
# # Task: Convert camelCase to snake_case.
# # Example Input: studentName
# # Example Output: student_name
# camel="studentName"
# snake=""
# for char in camel:
#     if char.isupper():
#         snake += "_" + char.lower()
#     else:
#         snake+=char
# print(snake)

# # 3. snake_case to camelCase
# # Definition: snake_case uses underscores; camelCase capitalizes later words.
# # Task: Convert snake_case to camelCase.
# # Example Input: student_name
# # Example Output: studentName
# snake="student_name"
# parts=snake.split("_")
# camel=parts[0]
# for part in parts[1:]:
#     camel+=part.capitalize()
# print(camel)

# # 4. Uppercase to Lowercase Definition: Uppercase letters are A-Z.
# # Task: Convert all uppercase letters to lowercase. 
# # Example Input: HELLO WORLD Example Output: hello world
# str=input("Enter string: ")
# result=""
# for ch in str:
#     if 'A'<=ch<='Z':
#         result+=chr(ord(ch)+32)
#     else:
#         result+=ch
# print(result)

# # 5. Lowercase to Uppercase Definition: Lowercase letters are a-z. 
# # Task: Convert all lowercase letters to uppercase.
# # Example Input: python Example Output: PYTHON
# str=input("Enter string: ")
# result=""
# for ch in str:
#     if 'a'<=ch<='z':
#         result+=chr(ord(ch)-32)
#     else:
#         result+=ch
# print(result)

# 6. Reverse Every Word Definition: Reverse each word only.
# Task: Reverse every word. 
# Example Input: Learn Python Example Output: nraeL nohtyP
# str=input("Enter string: ")
# words=str.split()
# for word in words:
#     i = len(word) - 1
#     while i >= 0:
#         print(word[i], end="")
#         i -= 1
#     print(end=" ")

# 7. Remove Duplicate Characters Definition: Keep first occurrence only. 
# Task: Remove duplicate characters.
# Example Input: programmingExample Output: progamin
# str=input("Enter string: ")
# result=""
# for ch in str:
#     if ch not in result:
#         result+=ch
# print(result)

# 8. Count Vowels and Consonants Definition: Count vowels and consonants. 
# Task: Print both counts.
# Example Input: Education Example Output: Vowels:5 Consonants:4
# s=input("Enter string: ").lower()
# vowels=0
# consonants=0
# for ch in s:
#     if ch.isalpha():
#         if ch in "aeiou":
#             vowels+=1
#         else:
#             consonants+=1
# print("Vowels:", vowels)
# print("Consonants:", consonants)

# 9. Replace Multiple Spaces Definition: Extra spaces should become one.
# Task: Replace multiple spaces with one. 
# Example Input: Python is fun Example Output: Python is fun
# str=input("Enter string: ")
# result=""
# space=False
# for ch in str:
#     if ch==" ":
#         if not space:
#             result+=ch
#             space=True
#     else:
#         result+=ch
#         space=False
# print(result)

# 10. Capitalize Every Word Definition: First letter uppercase.
# Task: Convert to title case.
# Example Input: welcome to python Example Output: Welcome To Python
# s=input("Enter string: ")
# words=s.split()
# for word in words:
#     print(word.capitalize(), end=" ")

# 11. Print Only Digits Definition: Digits are 0-9.
# Task: Extract digits. 
# Example Input: AB12CD345 Example Output: 12345
# s=input("Enter string: ")
# for ch in s:
#     if ch.isdigit():
#         print(ch, end="")

# 12. Print Only Alphabets Definition: Letters only. 
# Task: Remove digits and symbols. 
# Example Input: Pyt#123hon! Example Output: Python
# s=input("Enter string: ")
# for ch in s:
#     if ch.isalpha():
#         print(ch, end="")

# 13. Count Words Definition: Words separated by spaces. Task: Count words.
# Example Input: Python is easy to learn Example Output: 5
# s=input("Enter string: ")
# words = s.split()
# print(len(words))

# 14. Check Anagram Definition: Same letters, different order.
# Task: Check anagram. 
# Example Input: listen / silent Example Output: Anagram
# s1 = input("Enter first string: ")
# s2 = input("Enter second string: ")
# if sorted(s1) == sorted(s2):
#     print("Anagram")
# else:
#     print("Not Anagram")

# 15. Find Longest Word Definition: Longest word has most characters. 
# Task: Print longest word. 
# Example Input: I love programming language Example Output: programming
# s=input("Enter string: ")
# words=s.split()
# longest=words[0]
# for word in words:
#     if len(word)>len(longest):
#         longest=word
# print(longest)


# 16. Remove All Digits Definition: Digits are numeric chars. 
# Task: Remove all digits. 
# Example Input: Room12Block5 Example Output: RoomBlock
# s=input("Enter string: ")
# result=""
# for ch in s:
#     if not ch.isdigit():
#         result+=ch
# print(result)

# 17. Move Digits to End Definition: Keep letter order.
# Task: Move digits to end. 
# Example Input: A1B2C34 Example Output: ABC1234
# s=input("Enter string: ")
# letters=""
# digits=""
# for ch in s:
#     if ch.isdigit():
#         digits+=ch
#     else:
#         letters+=ch
# print(letters+digits)


# 18. Toggle Case Definition: Swap upper/lower.
# Task: Toggle every letter.
# Example Input: PyThOn Example Output: pYtHoN
# s=input("Enter string: ")
# result=""
# for ch in s:
#     if ch.islower():
#         result+=ch.upper()
#     elif ch.isupper():
#         result+=ch.lower()
#     else:
#         result+=ch
# print(result)

# 19. Palindrome Definition: Reads same both ways.
# Task: Check palindrome. 
# Example Input: madam Example Output: Palindrome
# s=input("Enter string: ")
# if s==s[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# 20. Compress Characters Definition: Consecutive repeats become char+count.
# Task: Compress string. 
# Example Input: aaabbccccdd Example Output: a3b2c4d2
# s=input("Enter string: ")
# result=""
# count=1
# for i in range(len(s)-1):
#     if s[i]==s[i + 1]:
#         count+=1
#     else:
#         result+=s[i]+str(count)
#         count=1
# result+=s[-1]+str(count)
# print(result)
