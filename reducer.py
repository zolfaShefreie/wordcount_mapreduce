#!/usr/bin/env python
import sys


if __name__ == "__main__":

    word_dict = dict()

    for line in sys.stdin:
        line = line.strip()
        word, count = line.split("\t", 1)
        
        try:
            count = int(count)
        except:
            continue
        
        word_dict[word] = word_dict.get(word, 0) + count
    
    word_dict = dict(sorted(word_dict.items(), key=lambda item: item[1], reverse=True))

    for word in word_dict:
        print('%s\t%s' % (word, word_dict[word]))