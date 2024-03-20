# 9. WEIGHTING WORD IMPORTANCE: 

    # You want a bag-of-words, but with words weighted by their importance to an observation. 
    # Compare the frequency of the word in a document (a tweet, a movie-review, speech transcript, etc..) with the frequency of the word in all other documents using ‘term frequency-inverse document frequency’ (tf-idf). 
    # Scikit learn makes this easy with TfidVectorizer:

# Load Libraries

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

# Create Text: 
text_data  = np.array(["I love Brazil. Brazil!",
                     "Sweden is best",  
                     "Germany beats both"])

# Create the tf-idf feature matrix: 

tfidf = TfidfVectorizer()    # weighting density. 
featurematrix = tfidf.fit_transform(text_data)
print(featurematrix)

# The output is a sparse matrix, However - if we want to view the output as a dense matrix, we can use .toarray()

array = featurematrix.toarray()  # type:ignore
print(array)

# Vocabulary_ shows us the word of each feature: 
voca = tfidf.vocabulary_
print(voca)

# ‘Term Frequency’ denotes the most number of occurrences of a word in a text document. 
# However, ‘Inverse Document Frequency’ denotes the less amount of importance that the words carries in a text document (word appears in many documents, it is likely less important to an any individual document).
# By combining these two statistics, we can assign a score to every word representing how important that word is in a document.
#  Specifically, we can multiply ‘tf’ to the inverse of the document frequency (idf) :   tf-idf (t,d) = tf(t,d) * idf(t) where t is a word and d is a document. 
# There are a number of variations in how tf and idf are calculated. 
# In Sci-kit learn, ‘tf’ is simply the number of times a word appears in the document. 
# But ‘idf’ is calculated as like the below formula where ‘nd’ is the number of documents and df(d,t) is a term, t’s document frequency (i.e., number of documents where the term appears). 
# By default, scikit-learn when nomalizes the tf-idf vectors using the Euclidean norm (L2 norm). 
# The higher the resulting value, the more important the words to a document. 
 

# Note: (Once find out the ‘idf’ by using the above formula - sklearn will go to the ‘L2 norm’ to find out the ‘df’ to get it’s inverse. 
       # Then it will use this ‘df’ to apply with the formula tf-idf (t,d) = tf(t,d) * idf(t) to finally find out the weightage of a word in a document)
