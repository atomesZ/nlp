import re
import spacy

# Loading the small English model
nlp = spacy.load("en_core_web_sm")

# A regexp that matches words only
re_word = re.compile(r"^\w+$")

def basic(text: str, remove_stopwords: bool = False) -> str:
    """
    Apply basic preprocessing to the given text
    
    Parameters
    ----------
    text : str
        The text to be preprocessed
       
    remove_stopwords : bool
        A boolean to choose if stopwords must be removed as well

    Returns
    -------
    string
        The preprocessed text
    """
    if remove_stopwords:
        tokens_str : list = [str(token) for token in nlp(text.lower()) if re_word.match(token.text) and not token.is_stop]
        return " ".join(tokens_str)
    else:
        # No processing
        return text


from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
nltk.download('stopwords')
nltk.download('punkt')

stop_words : set = set(stopwords.words('english'))
stemmer : SnowballStemmer = SnowballStemmer("english")

def stemming(text: str, remove_stopwords: bool = False) -> str:
    """
    Apply stemming preprocessing to the given text
    
    Parameters
    ----------
    text : str
        The text to be preprocessed
       
    remove_stopwords : bool
        A boolean to choose if stopwords must be removed as well

    Returns
    -------
    string
        The preprocessed text
    """
    stemmed : list = [stemmer.stem(word) for word in word_tokenize(text.lower()) if re_word.match(word) and not (remove_stopwords and word in stop_words)]
    return " ".join(stemmed)


def lemming(text: str, remove_stopwords: bool = False) -> str:
    """
    Apply lemming preprocessing to the given text
    
    Parameters
    ----------
    text : str
        The text to be preprocessed
       
    remove_stopwords : bool
        A boolean to choose if stopwords must be removed as well

    Returns
    -------
    string
        The preprocessed text
    """
    lemmas : list = [token.lemma_ for token in nlp(text.lower()) if re_word.match(token.text) and not (remove_stopwords and token.is_stop)]
    return " ".join(lemmas)

