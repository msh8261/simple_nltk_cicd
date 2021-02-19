import nltk
import json
import numpy as np
import re

nltk.download('tagsets', download_dir='/usr/local/share/')
nltk.download('stopwords', download_dir='/usr/local/share/')
wpt = nltk.WordPunctTokenizer()
stop_words = nltk.corpus.stopwords.words('english')

def normalize_document(doc):
    # lower case and remove special characters\whitespaces
    doc = re.sub(r'[^a-zA-Z\s]', '', doc, re.I|re.A)
    doc = doc.lower()
    doc = doc.strip()
    # tokenize document
    tokens = wpt.tokenize(doc)
    # filter stopwords out of document
    filtered_tokens = [token for token in tokens if token not in stop_words]
    # re-create document from filtered tokens
    doc = ' '.join(filtered_tokens)
    return doc

normalize_corpus = np.vectorize(normalize_document)


def lambda_handler(event, context):
    corpus = event["body"]
    norm_corpus = normalize_corpus(corpus)

    return {
        'statusCode': 200,
        'body': json.dumps(norm_corpus.tolist())
    }


# event = {"body": ['The sky is blue and beautiful.',
#                   'Love this blue and beautiful sky!',
#                   'The quick brown fox jumps over the lazy dog.',
#                   "A king's breakfast has sausages, ham, bacon, eggs, toast and beans",
#                   'I love green eggs, ham, sausages and bacon!',
#                   'The brown fox is quick and the blue dog is lazy!',
#                   'The sky is very blue and the sky is very beautiful today',
#                   'The dog is lazy but the brown fox is quick!'    
#             ]
#         }

# res = lambda_handler(event, '')

# print(res)




# from nltk.stem.porter import *

# p_stemmer = PorterStemmer()

# def lambda_handler(event, context):
#     words = event["body"]
#     list_ = []
#     for word in words:
#         print(word+' --> '+p_stemmer.stem(word))
#         list_.append(word+' --> '+p_stemmer.stem(word))
#     return {
#         'statusCode': 200,
#         'body': json.dumps(list_)
#     }


# event = {"body": ['run','runner','running','ran','runs','easily','fairly']}

# res = lambda_handler(event, '')

# print(res)