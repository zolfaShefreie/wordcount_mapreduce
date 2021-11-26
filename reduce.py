import sys


word_dict = dict()

for line in sys.stdin:
    line = line.strip()
    word, count = line.split("\t", 1)
    
    try:
        count = int(count)
    except:
        continue
    
    word_dict[word] = word_dict.get(word, 0) + count

for word in word_dict:
    print('%s\t%s' % (word, word_dict[word]))