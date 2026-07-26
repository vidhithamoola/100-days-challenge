# 1. Count Uppercase and Lowercase Letters 
# Definition: Uppercase letters are A–Z and lowercase letters are a–z. 
# Task: Read a string and print the number of uppercase and lowercase letters. 
# Example Input: PyTHon Example
# Output: Uppercase = 3 Lowercase = 3
str=input()
uppcount=0
lowcount=0
for char in str:
    if 65<=ord(char)<=90:
        uppcount += 1
    if 97<=ord(char)<=122:
        lowcount+=1
print(f"Uppercase={uppcount}")
print(f"Lowercase={lowcount}")

# 2. Longest Word Length Definition: A word is a sequence of characters separated by spaces. 
# Task: Read a sentence and print the length of the longest word. 
# Example Input: Python is amazing 
# Example Output: 7
sentence=input("Enter a sentence: ")
count=0
length=0
for character in sentence:
    if character !=" ":
        count+= 1
    else:
        if count>length:
            length=count
        count=0
if count>length:
    length=count
print(f"Longest word length = {length}")

# 3. Count Vowels in Even Positions Definition:
#     Vowels are a, e, i, o, u.
#     Task: Count vowels present at even index positions.
#     Example Input: Education
#     Example Output: 3
word=input("Enter a word: ")
vowels="aeiouAEIOU"
count=0
for i in range(0, len(word), 2):
    if word[i] in vowels:
        count+=1
print(f"Vowels at even positions = {count}")

# 4. Consecutive Duplicate Characters Definition: 
# Consecutive duplicate characters appear one after another. 
# Task: Count consecutive duplicate character pairs. 
# Example Input: bookkeeper 
# Example Output: 3
string=input() 
count=1
high=0 
same=0 
string_count=0 
for i in string:     
    string_count+=1 
    for idx in range(1,string_count):    
        if string[idx]==string[idx-1]:         
            count+=1     
        else:         
            if count>high:            
                high=count            
                same=1        
            elif count==high:             
                same+=1         
                count=1   
            if count>high:    
                    high=count     
                    same=1 
            elif count==high:    
                    same+1    
                    count=1           
                    print(same)
# 5. First Non-Repeating Character 
# # Definition: A non-repeating character appears exactly once.
# # Task: Print the first non-repeating character or Not Found. 
# # Example Input: swiss 
# # Example Output: w   
str=input() 
for i in str:     
    count=0     
    for k in string:         
        if i==k:            
            count+=1     
            if count==1:         
                print(i)          
                break

# 6. Longest Consecutive Vowel Sequence Definition:
#     A vowel sequence is consecutive vowels. 
#     Task: Find the longest consecutive vowel sequence. 
#     Example Input: beaautiful Example 
#     Output: 3
str1='beaautiful'
count=0
max_count =0
for i in str1:
    if i in "aeiouAEIOU":
        count+=1
        if count>max_count:
            max_count=count
else:
        count=0
print(max_count)

# 7. Character Frequency Definition:
#     Frequency is the number of occurrences. 
#     Task: Read a string and a character. Count its occurrences.
#     Example Input: programming g Example Output: 2
str1=input("Enter the string : ")
str2=input("Enter the char : ")
count=0
for i in str1:
    if str2==i:
        count+=1
print(count) 

# 8. Mirror String Check Definition: 
# A palindrome reads the same forwards and backwards.
# Task: Check whether the string is a palindrome.
# Example Input: madam 
# Example Output: Palindrome 
str1="madam"
rev=''
for i in str1:
    rev=i+rev
    if str1==rev:
        print("palindrome")
else:
    print("Not a palindrome")

# 9. Largest Alphabet Definition: The largest alphabet has the highest alphabetical order. 
# Task: Print the largest alphabet ignoring digits and symbols.
# Example Input: Pyth0n@Z 
# Example Output: Z
text=input('Enter the string:')
largest=""
for char in text:
    if ('A'<=char<='Z') or ('a'<=char<='z'):
        if largest=="":
            largest=char
        elif char>largest:
            largest=char
print(largest)

# 10. Compress Consecutive Characters Definition: Replace repeated consecutive characters with character followed by count. 
# Task: Compress the string. 
# Example Input: aaabbccccd
# Example Output: a3b2c4d1
text=input("Enter a string: ")
previous=""
count=0
for char in text:
    if previous=="":
        previous=char
        count=1
    elif char==previous:
        count+=1
    else:
        print(previous, count,sep="",end="")
        previous=char
        count=1
print(previous,count,sep="")