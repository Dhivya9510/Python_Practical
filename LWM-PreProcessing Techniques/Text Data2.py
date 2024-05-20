#  4.TOKENIZING TEXT:
   # Natural Language Toolkit of Python (NLTK) has a powerful set of text manipulation operators, including word tokenizing: 
   # Tokenizing is nothing but considering the each and every word in a sentence as a string in the form of list, so that we can convert it into the desire feature. 
# Import Library: 
import nltk
download = nltk.download('punkt')  # First just you need to download 'punkt' and check whether is it up-to-date or not? 
print(download)

# Load Library
from nltk import word_tokenize

# Create Text:
string = "The Science of Today is the Technology of Tommorow"

# Tokenize words: 
word_tokenizing = word_tokenize(string)
print(word_tokenizing)

# We can also tokenize into sentences: 
# Import Library: 
from nltk import sent_tokenize

# Create Text:
String2 = "The Science of Today is the Technology of Tommorow. Tommorow is today"

# Tokenize sentence: 
sent_tokenizing = sent_tokenize(String2)
print(sent_tokenizing)

# Tokenization, especially work tokenization is a common task after cleaning text data because it is the first step in the process of turning the text into the data we will use to construct useful features. 

# 5.	REMOVING STOP WORDS: 

    # Given Tokenized text data, you want to remove extremely common words (eg: a, is, on, of) that contains little informational value. 
    # Eliminating these kind of little amount informational things is generally known as ‘Removing Stop Words’. 

# Load Library:
import nltk
from nltk.corpus import stopwords  # ‘Stopwords’ package is available in ‘corpus’ as like ‘word/sent_tokenize’ package available in ‘Tokenize’. 

# you will have to download the set of stopwords first time
# Download ‘stopwords’ as like ‘punkt’ previously & check whether is it up-to-date or not? 

download2 = nltk.download("stopwords") 
print(download2) 

# Create word tokens:
tokenized_words = ['i','am','Going','to','go','to','the','Store','and','Park']

# Load Stop words:
stop_words = stopwords.words("english")

# Remove stop words.
Removed_stopwords = [word for word in tokenized_words if word not in stop_words ]  # understand the concept of this code. 
print(Removed_stopwords)

# While ‘stop words’ can refer to any set of words that we want to remove before processing, frequently the term refers to extremely common words that themselves contain little information value. 
# NLTK has a list of common stop words that we can use to find and remove stop words in our tokenized words. 
# Note that NLTK’s stopword assumes the tokenized words are all lowercased. (Not a problem if it is uppercased also as per my checkings)

# 6.	STEMMING WORDS: 
   
   # You have tokenized words and want to convert them into their root forms. 
   # (Multiple words denoted the same meaning – for that we enough to get that one word instead multiple words. 
   # It is useful to the reduction of words by find out the root words alone. In Tamil – we may heard about ‘Maruvudhal’ (root word). 

# Import Library
import nltk
from nltk.stem.porter import PorterStemmer

# Create word tokens: 
tokenized_words1 = ['i','am','humble','by','this','traditional','meeting']

# Create Stemmer 
porter = PorterStemmer()

# Apply stemmer: 
Application_of_stemmer = [porter.stem(word) for word in tokenized_words1]  # understand the concept of this code. 
print(Application_of_stemmer)

# Note: Mostly Using List comprehension only. 
       # Remember that ‘Tokenization’ is a simple and common task that we do after preprocessing and before giving it to the ML. 
       # Removed_stopwords = [word for word in tokenized_words if word not in stop_words ]  # understand the concept of this code.
       # Apply stemmer: 
               # [porter.stem(word) for word in tokenized_words1]  # understand the concept of this code.