#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Question 1- Write a Python program to replace all occurrences of a space, comma, or dot with a colon.


# In[9]:


import re
text='Python Exercises, PHP exercises.'
print(re.sub("[ ,.]",":",text))


# In[10]:


#Question 2-  Create a dataframe using the dictionary below and remove everything (commas (,), !, XXXX, ;, etc.) from the columns except words.


# In[5]:


import pandas as pd
import re
Dictionary={'SUMMARY' : ['hello, world!', 'XXXXX test', '123four, five:; six...']}

df=pd.DataFrame(Dictionary)

def clean_text(Dictionary):
 cleaned_text=re.sub(r'[^a-zA-Z\s]','',Dictionary)
 Cleaned_text= re.sub(r'\D+','',cleaned_text)

 return cleaned_text.strip()
df['SUMMARY']=df['SUMMARY'].apply(clean_text)

print(df)


# In[3]:


#Question 3- Create a function in python to find all words that are at least 4 characters long in a string. The use of the re.compile() method is mandatory.


# In[40]:


import re
string='hello data science'
pattern=re.compile(r'\b\w{4,}\b')
x=pattern.findall(string)
print(x)


# In[ ]:


#Question 4- Create a function in python to find all three, four, and five character words in a string. The use of the re.compile() method is mandatory.


# In[42]:


import re
string='hello dataa science'
pattern=re.compile(r'\b\w{3,5}\b')
x=pattern.findall(string)
print(x)


# In[ ]:


#Question 5- Create a function in Python to remove the parenthesis in a list of strings. The use of the re.compile() method is mandatory.


# In[158]:


import re
def remove_parentheses(strings):
    pattern = re.compile(r'\([^)]*\)')
    result = [pattern.sub(r'', s) for s in strings]
    return result
sample_text = ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
output = remove_parentheses(sample_text)
for item in output:
    print(item)


# In[ ]:


#Question 6- Write a python program to remove the parenthesis area from the text stored in the text file using Regular Expression.


# In[150]:


import re
def remove_parentheses(strings):
    pattern = re.compile(r'\([^)]*\)')
    result = [pattern.sub(r'', s) for s in strings]
    return result
sample_text = ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
output = remove_parentheses(sample_text)
for item in output:
    print(item)


# In[ ]:


#Question 7-Write a regular expression in Python to split a string into uppercase letters.
Sample text: “ImportanceOfRegularExpressionsInPython”


# In[159]:


import re

sample_text = "ImportanceOfRegularExpressionsInPython"

result = re.findall('[A-Z][a-z]*', sample_text)

print(result)


# In[ ]:


#Question 8- Create a function in python to insert spaces between words starting with numbers.


# In[168]:


import re
def insert_spaces(text):
    result = re.sub(r'(?<=[a-zA-Z])(\d)', r' \1', text)
    return result
sample_text = "RegularExpression1IsAn2ImportantTopic3InPython" 
output=insert_spaces(sample_text)
print(output)


# In[ ]:


#Question 9- Create a function in python to insert spaces between words starting with capital letters or with numbers.


# In[2]:


import re

def insert_spaces(text):
    
    result = re.sub(r'(?<=[a-zA-Z0-9])([A-Z0-9])', r' \1', text)
    return result

sample_text = "RegularExpression1IsAn2ImportantTopic3InPython"

output = insert_spaces(sample_text)

print(output)


# In[ ]:


#Question 10- Use the github link below to read the data and create a dataframe. After creating the dataframe extract the first 6 letters of each country and store in the dataframe under a new column called first_five_letters.


# In[9]:


import pandas as pd
github_link = 'https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv'
df = pd.read_csv(github_link)
df['first_five_letters'] = df['Country'].str[:6]


# In[ ]:


#Question 11- Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.


# In[5]:


import re

def is_valid_string(s):
    
    pattern = re.compile(r'^[a-zA-Z0-9_]+$')
    
    return bool(pattern.match(s))

test_strings = ["Valid_String123", "Invalid@String", "Another-Invalid", "123_underscore"]

for string in test_strings:
    print(f'{string}: {is_valid_string(string)}')


# In[ ]:


#Question 12- Write a Python program where a string will start with a specific number. 


# In[12]:


import re
string='123hello data science'
pattern=re.compile(r'^[a-zA-Z0-9_]+\d*')
x=pattern.findall(string)
print(x)


# In[42]:


#Question 13- Write a Python program to remove leading zeros from an IP address


# In[44]:


import ipaddress

def remove_leading_zeros(str):
    
  regex = "^0+(?!$)"
str1 = "192.168.001.001"
str = re.sub(regex,"",str1)

print(str)


# In[ ]:


#Question 15- Write a Python program to search some literals strings in a string. 
Sample text : 'The quick brown fox jumps over the lazy dog.'
Searched words : 'fox', 'dog', 'horse'


# In[46]:


def search_words(text, words):
    found_words = [word for word in words if word in text]
    return found_words

sample_text = 'The quick brown fox jumps over the lazy dog.'
searched_words = ['fox', 'dog', 'horse']

found_words = search_words(sample_text, searched_words)

print(found_words)


# In[ ]:


#Question 16- Write a Python program to search a literals string in a string and also find the location within the original string where the pattern occurs
Sample text : 'The quick brown fox jumps over the lazy dog.'
Searched words : 'fox'


# In[47]:


def search_word_location(text, word):
    location = text.find(word)
    return location

sample_text = 'The quick brown fox jumps over the lazy dog.'
searched_word = 'fox'

location = search_word_location(sample_text, searched_word)
print(location)


# In[ ]:


#Question 17- Write a Python program to find the substrings within a string.
Sample text : 'Python exercises, PHP exercises, C# exercises'
Pattern : 'exercises'.


# In[2]:


import re

def find_substrings(input_string, pattern):
    
    matches = re.findall(pattern, input_string)

    return matches


sample_text = 'Python exercises, PHP exercises, C# exercises'


pattern_to_find = 'exercises'


result = find_substrings(sample_text, pattern_to_find)


print(f"Occurrences of '{pattern_to_find}' in the text: {result}")


# In[3]:


#Question 18- Write a Python program to find the occurrence and position of the substrings within a string.


# In[4]:


import re
text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print('Found "%s" at %d:%d' % (text[s:e], s, e))


# In[ ]:


#Question 19- Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.


# In[10]:


import re

def find_decimal_numbers(input_string):
    pattern = re.compile(r'\b\d+\.\d{1,2}\b')
    matches = pattern.findall(input_string)
    return matches

def main():
    sample_text = "01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"
    result = find_decimal_numbers(sample_text)
    
        print


# In[ ]:


#Question 21- Write a Python program to separate and print the numbers and their position of a given string.


# In[13]:


import re
# Input.
text = "data science 23"

for m in re.finditer("\d+", text):
    print(m.group(0))
    print("Index position:", m.start())


# In[ ]:





# In[ ]:





# In[ ]:




