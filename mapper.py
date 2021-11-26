import sys
import re


class TextCleaner:
    punc = '''!()-[]{.};:'"\,<>/?@#$%^&*_~'''
    
    def run(text: str) -> list:
        """
            run textCleaner for input string
        Args:
            text (str): input string

        Returns:
            list: token list
        """
        pass
    
    def tokenize(text: str) -> list:
        pass
    
    @classmethod
    def normlize(cls, text: str) -> str:
        """

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
        
    
    def remove_stopwords(tokens: list) -> list:
        pass


if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        words = line.split()
        for word in words:
            print('%s\t%s' % (word, 1))