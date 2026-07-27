 # 1. Longest Consecutive Consonant Sequence Definition: A consonant sequence is a group of consecutive consonants without any vowels in between. 
# # Task: Read a string and print the length of the longest consecutive consonant sequence. 
# # Example Input: strength 
# # Example Output: 4
# str=input()  
# name="" 
# lon_count=0 
# count=0  
# for ch in str:      
#     if ch=='a'or ch=='e' or ch=='i' or ch=='o' or ch=='u':         
#         count=0     
#     else:         
#         count+=1      
#         if count>lon_count:         
#             lon_count=count  
#             print(lon_count)   

# # 2. Alternate Case Check Definition: A string has alternating case if every adjacent pair of letters has different cases. 
# # Task: Read a string containing only alphabets and determine whether its letters alternate between uppercase and lowercase.
# # Example Input: pYtHoN 
# # Example Output: Alternating  
# s=input("Enter a string: ")
# for i in range(len(s)-1):
#     if (s[i].isupper() and s[i + 1].isupper()) or (s[i].islower() and s[i + 1].islower()):
#         print("Not Alternating")
#         break
# else:
#     print("Alternating")

# # 3. Most Frequent Character Definition: The most frequent character is the one that appears the highest number of times. 
# # Task: Read a string and print the character with the highest frequency.
# # If there is a tie, print the one that appears first. 
# # Example Input: mississippi Example Output i
# s=input("Enter a string: ")
# max_count=0
# chr=""
# for k in range(len(s)):
#     count=0
#     for n in range(len(s)):
#         if s[k]==s[n]:
#             count=count+1
#     if count>max_count:
#         max_count=count
#         chr=s[k]
# print(chr)

# 4. Count Words Starting with a Vowel 
# Definition: A word starts with a vowel if its first letter is A, E, I, O, or U. 
# Task: Read a sentence and count how many words begin with a vowel. 
# Example Input: Apple is an orange Example Output: 4
# str=input("Enter a sentence: ")
# words=str.split()
# count=0
# for word in words:
#     if word[0]=='A' or word[0]=='E' or word[0]=='I' or word[0]=='O' or word[0]=='U' or word[0]=='a'or word[0]=='e' or word[0]=='i' or word[0]=='o' or word[0]=='u':
#         count=count + 1
# print(count)

# 5. Remove Consecutive Duplicates Definition: If the same character appears repeatedly next to itself, keep only one occurrence.
# Task: Read a string and print the modified string. 
# Example Input: aaabbbccaadd 
# Example Output: abcad
# s=input("Enter a string: ")
# result=s[0]
# for i in range(1,len(s)):
#     if s[i]!=s[i-1]:
#         result=result+s[i]
# print(result)

# 6. Longest WordDefinition: The longest word is the word with the maximum number of characters. 
# Task: Read a sentence and print the longest word. If multiple words have the same length, print the first one. 
# Example Input: Python programming is interesting 
# Example Output: programming
# s=input("Enter a sentence: ")
# words=s.split()
# longest=words[0]
# for word in words:
#     if len(word)>len(longest):
#         longest=word
# print(longest)

# 7. Count Character Changes Definition: A character change occurs when the current character differs from the previous one. 
# Task: Read a string and count how many character changes occur. 
# Example Input: aaabbccdaa Example Output: 
# s1=input() 
# count=0
# for ch in range(len(s1)-1): 
#     if s1[ch]!=s1[ch+1]: 
#         count+=1 
#         print(count)

# 8. Rotate String Left by One Position Definition: Left rotation moves the first character to the end.
# Task: Read a string and print its left rotation. 
# Example Input: python 
# Example Output: ythonp 
# n=input() 
# rot="" 
# frst=n[0] 
# for i in range(len(n)): 
#     if i==0: 
#         continue 
#     else: 
#         rot+=n[i] 
#         rot+=frst
#         print(rot)
        
# 9. Largest Alphabetical Word Definition: The largest alphabetical word is the word that comes last in dictionary order. 
# Task: Read a sentence and print the largest alphabetical word. 
# Example Input: apple mango zebra orange 
# Example Output: zebra
# str=input("Enter a sentence: ")
# words=str.split()
# largest=words[0]
# for word in words:
#     if word>largest:
#         largest=word
# print(largest)

# 10. Count Palindromic Words Definition: A palindromic word reads the same forward and backward. 
# Task: Read a sentence and count how many words are palindromes.
# Example Input: madam level python radar Example Output: 3
# s=input("Enter a sentence: ")
# words=s.split()
# count=0
# for word in words:
#     if word==word[::-1]:
#         count=count+1
# print(count)