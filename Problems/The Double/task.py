# put your python code here
import string
# put your python code here

keys = []
values = []
alphabet = string.ascii_lowercase
for letter in alphabet:
    keys.append(letter)
    
for double_letter in alphabet:
    values.append(double_letter * 2)
    

double_alphabet = dict(zip(keys, values))
# print(double_alphabet)
