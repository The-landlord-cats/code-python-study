word = {'s': 5 ,'d' : 4}
print(sorted(word.items(), key= lambda x:x[1], reverse=False))