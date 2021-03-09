# put your python code here
sentence = input().lower().split()

word_count_dict = {}
for word in sentence:
    if word in word_count_dict:
        word_count_dict[word] += 1
    else:
        word_count_dict[word] = 1


for k, v in word_count_dict.items():
    print(k, v)
