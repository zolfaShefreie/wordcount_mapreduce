#!/usr/bin/env python
import sys
import re
import os


def get_stopwords():
    """read stopwords from file

    Returns:
        [type]: [description]
    """
    path = '/home/hadoop/hadoop/bin/wordcount_mapreduce/stopwords'
    #print(path)
    f = open(path, encoding='utf-8')
    words = f.read()
    return set([w for w in words.split('\n') if w])


class TextCleaner:
    
    punc = '''!()-[]{.};:'"\,<>/?@#$%^&*_~`|’'''
    removed_plus = ['u', ] + list(get_stopwords())
    
    @classmethod
    def run(cls, text: str) -> list:
        """
            run textCleaner for input string
        Args:
            text (str): input string

        Returns:
            list: token list
        """
        return cls.tokenize(cls.normlize(text))
    
    @classmethod
    def tokenize(cls, text: str) -> list:
        """
            tokenize, delete eng stopwords
        Args:
            text (str): input string

        Returns:
            list: tokens
        """
        
        #stop_words = list(stopwords.words("english")) + cls.removed_plus
        #tokens = word_tokenize(text)
        stop_words = cls.removed_plus
        tokens = text.split()
        return [token.strip() for token in tokens if token.strip() and token.strip() not in stop_words]
            
    
    @classmethod
    def normlize(cls, text: str) -> str:
        """
            lower, delete numbers, delete punc, strip
        Args:
            text (str): input string

        Returns:
            str: normlized string
        """
        text = text.lower()
        text = re.sub(r"\d+", '', text)
        
        for each in cls.punc:
            text = text.replace(each, " ")
        
        text.strip()
        
        return text


if __name__ == "__main__":
    """
    mapper
    """
    
    text_cleaner = TextCleaner()
    
    for line in sys.stdin:
        words = text_cleaner.run(line)
        for word in words:
            print('%s\t%s' % (word, 1))