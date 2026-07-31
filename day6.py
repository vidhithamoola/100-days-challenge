# 1. Longest Repeating Character Block Definition A repeating character block is a sequence of consecutive identical characters.
# Task Read a string and print: 
# The character having the longest consecutive block. The length of that block. 
# Example Input aaabccccddbb Example Output Character = c Length = 4
# str=input("Enter a string: ")
# i=0
# maxchar=""
# maxlen=0
# while i<len(str):
#     count=1
#     while i+1<len(str) and str[i]==str[i + 1]:
#         count+=1
#         i+=1
#     if count>maxlen:
#         maxlen=count
#         maxchar=str[i]
#     i+=1
# print("Character =", maxchar)
# print("Length =", maxlen)
# 2. Characters Between Two Letters Definition The characters between two occurrences are those lying strictly between them.
# Task Read a string and a character. Print the number of characters between the first and last occurrence of that character.
# If the character appears fewer than two times, print -1.
# Example Input programming g Example Output 5 
# str= input("Enter a string: ")
# chr=input("Enter a character: ")
# first=-1
# last=-1
# for i in range(len(str)):
#     if str[i]==chr:
#         if first==-1:
#             first=i
#         last=i
# if first==-1 or first==last:
#     print(-1)
# else:
#     print(last-first-1)
# 3. Word With Maximum Vowels Definition The vowel count of a word is the number of vowels present in it. 
# Task Read a sentence and print the word containing the maximum number of vowels. 
# If there is a tie, print the first one. 
# Example Input education makes learning enjoyable Example Output education.
# str=input("Enter a sentence: ")
# word=""
# maxword=""
# maxvowels=0
# for chr in str+" ":
#     if chr!=" ":
#         word+=chr
#     else:
#         count=0
#         for chr in word:
#             if chr in "aeiouAEIOU":
#                 count+=1
#         if count>maxvowels:
#             maxvowels=count
#             maxword=word
#         word=""
# print(maxword)
# 4. Consecutive Alphabet Check Definition Two letters are consecutive if their ASCII values differ by exactly 1. 
# Task Read a string and determine whether every adjacent pair of characters is consecutive.
# Example Input abcde Example Output Yes 
# str=input("Enter a string: ")
# for i in range(len(str)-1):
#     if ord(str[i+1])-ord(str[i])!=1:
#         print("No")
#         break
# else:
#     print("Yes")
# 5. Reverse Every Word Definition Each word is reversed individua ly while keeping the order of words unchanged. 
# Task Read a sentence and print the modified sentence. 
# Example Input learn python today Example Output nrael nohtyp yadot
# str=input("Enter a sentence: ")
# temp=""
# for chr in str:
#     if chr !=" ":
#         temp=chr+temp
#     else:
#         print(temp,end=" ")
#         temp=""
# print(temp)
# 6. Most Frequent Vowel Definition The most frequent vowel is the vowel that appears the greatest number of times. 
# Task Read a string and print the vowel with the highest frequency. 
# If there are no vowels, print No Vowels. 
# str=input("Enter a string: ")
# vowels="aeiou"
# maxvowel=""
# maxcount=0
# for chr in vowels:
#     if str.count(chr)>maxcount:
#         maxcount=str.count(chr)
#         maxvowel=chr
# if maxcount==0:
#     print("No Vowels")
# else:
#     print(maxvowel)
# 7. Equal Vowels and Consonants Definition A string is balanced if it contains the same number of vowels and consonants.
# # Task Read a string containing only alphabets. Print whether it is balanced. 
# # Example Input code Example Output Balanced
# text=input("Enter a string: ").lower()
# vow="aeiou"
# vowcount=0
# conscount=0
# for char in text:
#     if char in vow:
#         vowcount+=1
#     else:
#         conscount+=1
#         if vowcount==conscount:
#             print("Balanced")
#         else:
#             print("Not Balanced")
#8. Mirror Half Check Definition The first half of the string should match the reverse of the second half. 
# Task Read an even-length string and determine whether it satisfies this condition. 
# # Example Input abccba Example Output Yes
# str=input("Enter a string: ")
# mid=len(str)//2
# fir=str[:mid]
# sec=str[mid:]
# if fir==sec[::-1]:
#     print("Yes")
# else:
#     print("No")
# 9. Count Valid Identifier Characters Definition A valid identifier character is: A-Z a-z 0-9 _ (underscore)
# Task Read a string and count how many valid identifier characters it contains.
# Example Input user_name@123 Example Output 12
# str=input("Enter a string: ")
# count=0
# for chr in str:
#     if ('A'<=chr<='Z')or('a'<=chr<='z')or('0'<=chr<='9')or chr=='_':
#         count+=1
# print(count)
