import re
import spacy

# loading the small English model
nlp = spacy.load("en_core_web_sm")

re_word = re.compile(r"^\w+$")

def basic(text: str, remove_stopwords: bool = False) -> str:
    if remove_stopwords:
        tokens_str = [str(token) for token in nlp(text.lower()) if re_word.match(token.text) and not token.is_stop]
        return " ".join(tokens_str)
    else:
        # No processing
        return text


from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))
stemmer = SnowballStemmer("english")

def stemming(text: str, remove_stopwords: bool = False) -> str:
    stemmed = [stemmer.stem(word) for word in word_tokenize(text.lower()) if re_word.match(word) and not (remove_stopwords and word in stop_words)]
    return " ".join(stemmed)


def lemming(text: str, remove_stopwords: bool = False) -> str:
    lemmas = [token.lemma_ for token in nlp(text.lower()) if re_word.match(token.text) and not (remove_stopwords and token.is_stop)]
    return " ".join(lemmas)

