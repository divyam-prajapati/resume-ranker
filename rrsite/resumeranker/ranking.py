from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from nltk import word_tokenize          
from nltk.stem import WordNetLemmatizer
import nltk
from nltk.corpus import stopwords

# Download stopwords list, puncutations, wordnet corpus
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('omw-1.4')

stop_words = set(stopwords.words('english')) 

# Interface lemma tokenizer from nltk with sklearn
class LemmaTokenizer:
    ignore_tokens = [',', '.', ';', ':', '"', '``', "''", '`']
    def __init__(self):
        self.wnl = WordNetLemmatizer()
    def __call__(self, doc):
        return [self.wnl.lemmatize(t) for t in word_tokenize(doc) if t not in self.ignore_tokens]

def rank(search_terms, objects):

    # Appending documents array
    dict={}
    documents = []
    for o in objects:
        dict[o.id] = []
        documents.append(o.text)

    # Lemmatize the stop words
    tokenizer=LemmaTokenizer()
    token_stop = tokenizer(' '.join(stop_words))

    # Create TF-idf model
    vectorizer = TfidfVectorizer(stop_words=token_stop, tokenizer=tokenizer)
    doc_vectors = vectorizer.fit_transform([search_terms] + documents)

    # Calculate similarity
    cosine_similarities = linear_kernel(doc_vectors[0:1], doc_vectors).flatten()
    document_scores = [item.item() for item in cosine_similarities[1:]]
    
    # Storing Data in dict Dictionary
    document_scores = [round(x * 100) for x in document_scores]
    count=0
    for d in dict.keys():
        dict[d] = (document_scores[count])
        count+=1
    RESULTS=[]
    document_scores=sorted(document_scores, reverse=True)
    for d in document_scores:
        RESULTS.append(get_key(dict, d))

    
    # print("\n********************************************")
    # print(dict)
    # print("********************************************")
    # print(RESULTS)
    # print("********************************************\n")

    return(RESULTS)


def get_key(my_dict, val):
    for key, value in my_dict.items():
        if val == value:
            return key

# dict = {
#     "11": 0.267896,
#     "12": 0.507896,
#     "13": 0.207896,
#     "14": 0.907896
# }
