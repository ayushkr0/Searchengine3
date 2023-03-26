from flask import Flask, request, jsonify
import PyPDF2
from pdfminer.high_level import extract_text

app = Flask(__name__)

@app.route('/api', methods=['POST'])

def matchingWords(query, text):
    sentences = text.split(".")
    score = [0]*len(sentences)
    
    for i, sentence in enumerate(sentences):
        words = sentence.split()
        for word in words:
            if query.lower() == word.lower():
                score[i] += 1
    
    sortedSentScore = [sentScore for sentScore in sorted(zip(score,sentences), reverse=True)]
    return sortedSentScore



def work(query):
    pdf_file = open("pdf1.pdf", 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    # text = ""
    text = extract_text("pdf2.pdf")
    print(text) 

    # print(text)

    sortedSentScore = matchingWords(query, text)

    print(f"{len(sortedSentScore)} Result found!")
    for score, item in sortedSentScore:
        print(f"\"{item}\": with a score of {score}")
    return sortedSentScore

# global query
def api():
    data = request.get_json()

    query = data['text']
    num = int(data['num'])

    return jsonify(query)
    # processed_text = text.upper() + ' ' + str(num)
    # response = {
    #     'result': 'success',
    #     'processed_text': processed_text,
    #     'url': request.url
    # }
    # return jsonify(response)



if __name__ == "__main__":
    # pdf_file = open("pdf1.pdf", 'rb')
    # pdf_reader = PyPDF2.PdfReader(pdf_file)
    # text = ""
    # for page in pdf_reader.pages:
    #     text += page.extract_text()

    # print(text)

    # query = input("Please enter the query\n")
    # sortedSentScore = matchingWords(query, text)
    # print(f"{len(sortedSentScore)} Result found!")
    # for score, item in sortedSentScore:
    #     print(f"\"{item}\": with a score of {score}")
    print("Working")
    app.run(debug=True)
