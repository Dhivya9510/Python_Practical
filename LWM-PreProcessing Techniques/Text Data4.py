# 8.ENCODING TEXT AS A BAG OF WORDS:

    # As you understood by the title - it encoding each and every text inside the bulk of words to the features. 
    
# Load Library:
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

# Create Text: 
text_data = np.array(["I love Brazil. Brazil!",
                     "Sweden is best",  
                     "Germany beats both"])

# Create bag of words feature matrix: 
count = CountVectorizer()
bag_of_words = count.fit_transform(text_data)
print(bag_of_words)

   # This output is a sparse array (Sparse Matrix is the matrix that also contains Zeros), which is often neccessary when we have a large amount of text. 
   # However in our toy example we can only use 'toarray' to view a matrix of word counts for each observation. 

toydata = bag_of_words.toarray()  # type:ignore
print(toydata)
   
    # The output may be confused you. For a clarity - get the feature_matrix, so that you can compare yourself to get clarity. 
    # That means we can use 'Vocubulary_method' to view the word associated with each feature: 

feature = count.get_feature_names_out()
print(feature)

# One of the most common methods of transforming text in to features is by using a ‘bag-of-words’ model. 
#‘bag-of-words’ model output a feature for every unique word in text data, with each feature containing a count of occurrences in observations. 
# Here in our example – the text data was purposely small – In the real world, a single observation of text data could be the contents of an entire book. 
# Since our ‘bag of words’ model creates a feature for every unique word in the data, the resulting matrix can contain thousands of features. 
# This means that the size of the matrix can sometimes become very large in memory. 
# However, luckily, we can exploit a common characteristic of bag-of-words feature matrices to reduce the amount of data we need to store. 

# Most words likely do not occur in most observations, and therefore bag-of-words feature matrices will contain mostly 0s as values. 
# We call these types of matrices ‘sparse’. Instead of storing all values of the matrix, we can only store nonzero values and then assume all other values are 0. 
# This will save us memory when we have large feature matrices. 

# One of the nice features of ‘CountVectorizer’ is that the output is a sparse matrix by default. 
# CountVectorizer comes with a number of useful parameters to make creating bag-of-words feature matrices easy. 
# First, while by default every feature is a word, that does not have to be the case. 
# Instead, we can set every feature to be the combination of two words (called a 2-gram) or even three words (3-gram). 

# ngram_range sets the minimum and maximum size of our n-grams. 
# For example, (2,3) will return all 2-grams and 3- grams. 
# Second, we can easily remove low-information filler words using stop_words either with a built-in list or a custom list. 
# Finally, we can restrict the words or phrases we want to consider to a certain list of words using vocabulary. For example, we could create a ‘bag-of-words’ feature matrix for only occurrences of country names: 

# Create feature matrix with arguements: 

count_2grams = CountVectorizer(ngram_range=(1,2), stop_words="english", vocabulary= ["Brazil"])  
      # Here we asked to eliminate the ngram 0 & taking 'stop_words' into account for getting less information by memory optimization. 
      # And we restrict the word 'Brazil' hence the output showing as 0. 

bag = count_2grams.fit_transform(text_data)
array = bag.toarray() #type: ignore
print(array)

voca = count_2grams.vocabulary_
print(voca)

# GENERATE THE N-GRAMS FOR THE GIVEN SENTENCES: 

import nltk
from nltk.util import ngrams

# Function to generate n-grams from sentences: 

def extract_ngrams(data, num):
    n_grams = ngrams(nltk.word_tokenize(data),num)
    return(' '.join(grams) for grams in n_grams)

data = "A class is a blueprint for the object"

print("1-gram:" , extract_ngrams(data, 1))
print("2-gram:" , extract_ngrams(data, 2))
print("3-gram:" , extract_ngrams(data, 3))
print("4-gram:" , extract_ngrams(data, 4))

# Note: (Understand the important function code for generating n-grams from sentences from the line 72 to 78)