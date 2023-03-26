from flask import Flask, jsonify, request
import PyPDF2
from pdfminer.high_level import extract_text
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
import time
import numpy as np
from collections import Counter


app = Flask(_name_)

start = time.time()
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


def similarity_score(s1, s2):
    set1 = set(s1.split())
    set2 = set(s2.split())
    intersection = len(set1 & set2)
    union = len(set1 | set2)
    return intersection / union

    return score


@app.route('/api', methods=['POST'])
def api():
    data = request.get_json()
    query = data['text']

    pdf_files = glob.glob("*.pdf")
    text = []

    for i in pdf_files:
        temp = extract_text(i)
        text.append(temp)

    new_text = []
    score = []
    ssscore = []

    for i in text:
        new_text.append(preprocess_text(i))

    text1 = query
    text1=preprocess_text(text1)

    for i in new_text:
        score.append(similarity_score(text1, i))

    new_list = np.array(list(zip(pdf_files, score * 100)))

    sample = np.array(new_list)
    Array_sort = sample[sample[:, 1].argsort()]
    final_list = Array_sort.tolist()

    final = []
    for i, j in final_list:
        final.append(i)
    # response = {
    #     'result': 'success',
    #     'url': request.url
    # }

    return jsonify(final)


if _name_ == "_main_":
    app.run(debug=True)
