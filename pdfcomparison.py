import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem import SnowballStemmer, WordNetLemmatizer
import string
import math
import re
from pdfminer.high_level import extract_text
import glob
import json
pdf_files = glob.glob("*.pdf")
ss = []
stop_words = set(stopwords.words('english'))
stemmer = SnowballStemmer('english')
lemmatizer = WordNetLemmatizer()
tokenizer = RegexpTokenizer(r'\w+')

def preprocess_text(text):
        text = re.sub('[^a-zA-Z0-9\s]', '', text)
        words = tokenizer.tokenize(text)
        words = [word for word in words if word.lower() not in stop_words]
        words = [word.lower() for word in words]
        words = [stemmer.stem(word) for word in words]
        words = [lemmatizer.lemmatize(word) for word in words]
        text = ' '.join(words)
        return text



pp="pdf_1.pdf"
text1 = extract_text(pp)
for i in pdf_files:

    text2 = extract_text(i)
    
    
    newtext1 = preprocess_text(text1)
    newtext2 = preprocess_text(text2)


    def jaccard_similarity(text1, text2):
        set1 = set(text1.split())
        set2 = set(text2.split())

        intersection = len(set1.intersection(set2))
        union = len(set1.union(set2))
        similarity = intersection / union
        return similarity

    ss.append(jaccard_similarity(text1, text2))



new=[]
for i in ss:
    new.append(round(i*100))



max=max(new)
if(max < 15 ):
    print("yes")
else:
    print("no")