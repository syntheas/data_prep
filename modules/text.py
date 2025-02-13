#Text  Cleaning
import re
import contractions
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import string
import regex

# Define stop words for text cleaning
stop_words = set(stopwords.words('english'))
custom_stop_words = {"hello", "hi", "please"}
custom_stop_words.update(stop_words)

# Initialize lemmatizer for text cleaning
lemmatizer = WordNetLemmatizer()


def strip_all_entities(body):
    body = re.sub(r'\r|\n', ' ', body.lower())  # Replace newline and carriage return with space, and convert to lowercase
    body = re.sub(r"(?:\@|https?\://)\S+", "", body)  # Remove links
    body = re.sub(r'[^\x00-\x7f]', '', body)  # Remove non-ASCII characters
    banned_list = string.punctuation
    table = str.maketrans('', '', banned_list)
    body = body.translate(table)
    body = ' '.join(word for word in body.split() if word not in custom_stop_words)
    return body

# Filter special characters such as & and $ present in some words
def filter_chars(body):
    return ' '.join('' if ('$' in word) or ('&' in word) else word for word in body.split())

# Remove multiple spaces
def remove_mult_spaces(body):
    return re.sub(r"\s\s+", " ", body)
# Expand contractions
def expand_contractions(body):
    return contractions.fix(body)
# remove stopwords
def remove_stopwords(text):
    words = word_tokenize(text)
    filtered_text = [word for word in words if word.lower() not in custom_stop_words]
    
    return " ".join(filtered_text)
# Remove numbers
def remove_numbers(body):
    return re.sub(r'\d+', '', body)
# Lemmatize words
def lemmatize(body):
    words = word_tokenize(body)
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
    return ' '.join(lemmatized_words)
# Remove short words
def remove_short_words(body, min_len=2):
    words = body.split()
    long_words = [word for word in words if len(word) >= min_len]
    return ' '.join(long_words)
# Replace elongated words with their base form
def replace_elongated_words(body):
    regex_pattern = r'\b(\w+)((\w)\3{2,})(\w*)\b'
    return re.sub(regex_pattern, r'\1\3\4', body)
# Remove repeated punctuation
def remove_repeated_punctuation(body):
    return re.sub(r'[\?\.\!]+(?=[\?\.\!])', '', body)
# Remove extra whitespace
def remove_extra_whitespace(body):
    return ' '.join(body.split())
def remove_url_shorteners(body):
    return re.sub(r'(?:http[s]?://)?(?:www\.)?(?:bit\.ly|goo\.gl|t\.co|tinyurl\.com|tr\.im|is\.gd|cli\.gs|u\.nu|url\.ie|tiny\.cc|alturl\.com|ow\.ly|bit\.do|adoro\.to)\S+', '', body)
# Remove short  tickets
def remove_short_words(ticket, min_words=0):    # We do not need this , real data world is not forgiving
    words = ticket.split()
    return ticket if len(words) >= min_words else ""

def remove_consecutive_word_groups(txt):
    txt = txt + ' '
    RE = regex.compile(r'\b((?:\p{L}+\s+)+)(?:\1)')
    # Function to apply regex replacement
    def replace_func(match):
        return match.group(1)

    # Apply the regex replacement iteratively until no changes are made
    while True:
        new_text, count = RE.subn(replace_func, txt)
        if count == 0:
            break
        txt = new_text

    return txt.strip()