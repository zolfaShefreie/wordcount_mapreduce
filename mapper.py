import sys
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


class TextCleaner:
    
    punc = '''!()-[]{.};:'"\,<>/?@#$%^&*_~'''
    
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
        
        stop_words = set(stopwords.words("english"))
        tokens = word_tokenize(text)
        return [token for token in tokens if token not in stop_words]
            
    
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
            text = text.replace(each, "")
        
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