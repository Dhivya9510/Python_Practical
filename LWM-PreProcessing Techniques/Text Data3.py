# TAGGING PARTS OF SPEECH

   # (To find out the parts of speech in a sentence. That is – Noun, Pronoun, Verb, Adverb, Adjective, Preposition, Conjunction & Interjection).
   # Here download ‘Averaged_Perceptron_Tagger’ and check whether is it up-to-date or not!
   # Here we use the package named ‘pos_tag’.  It’s actually a ‘pre-trained parts of speech tagger’. Hence, we don’t need to train anything, we only have to input our word tokens to process. 
   # The output returned as like a ‘tuple’ datatype. 


# Import Library
import nltk
tags = nltk.download('averaged_perceptron_tagger')
print(tags)  # It shows up-to-dated or not. 

# Load Libraries: 
from nltk import pos_tag
from nltk import word_tokenize

# Create text:
text_data = "Chris loved outdoor running"

# Use pre-trained parts of speech tagger. (pos_tag)
text_tagged = pos_tag(word_tokenize(text_data))  # Note here 'pos_tag' is alonged with 'word_tokenize'.
print(text_tagged)

# The output is a list of tuples with the word and the tag of the parts of speech. 
# NLTK uses the 'Penn Treebank' parts of speech tags (like abbreviations as below)
# Some examples of the Penn Treebank tags are: 
     # NNP - Proper noun, Singular
     # NN - Noun, Singular or mass
     # NNS - Noun, Plural
     # NNPS - Proper noun, Plural. 
     # RB - Adverb
     # VBD - Verb, Past tense
     # VBG - Verb , Gerund or present participle.
     # JJ - Adjective
     # PRP - Personal Pronoun. 
# Once the text has been tagged, we can use the tags  to find certain parts of speech. For example here are all the nouns. 

# a) Filter words: 
filter = [word for word,tag in text_tagged if tag in ['NN','NNS','NNP','NNPS']]  # (These are all posibilities of Noun, we can also give their respective possibilities). 
print(filter)

# Just note the below code with my own remembering format. 
    # We need words as output first of all. So, write ‘word for word’.                                                                                      Now, we asked to find the same pos mentioned in the list bracket from the tags in ‘text tagged’ (that is the variable where we found out the pos for given input). 
    # So, we write look for ‘tag’ in ‘text_tagged’ only if tag similar to []

# A more realistic situation would be that we have data where every observation contains a tweet and we want to convert those sentences into features for individual pos.
# Example, a feature with 1 if a proper noun is present and 0 otherwise. 

# b) Create Text: 
tweets = ["I am eating a burrito for breakfast", "Political science is an amazing field", "San Fransisco is an awesome city. "]
# Create List: 
tagged_tweets = []
# Tag each word and each tweet. 
for tweet in tweets: 
    tweet_tags = nltk.pos_tag(word_tokenize(tweet))
    tagged_tweets.append(tag for word, tag in tweet_tags)

# For the below own written code as per video without using pre-built ‘pos_tag’ - note the code with my own remembering format. 
    # First line: create a variable named tweet (for tweet in tweets)
    # Second line: we create our own, so write nltk with pos_tag.  ‘nltk.pos_tag(word_tokenize(tweet)), here we put our own created variable. 
    # Third line: We need to append the tag of (our second line variable) with list variable. Here we need word, so put ‘tag for word’. 

# c) Use one-hot encoding to convert the tags into features: 
     # Here we have multiple labels. so we going to use 'Mulitple Binarizer'.
    
import sklearn
from sklearn.preprocessing import MultiLabelBinarizer

one_hot_multiBin = MultiLabelBinarizer()
variable = one_hot_multiBin.fit_transform(tagged_tweets)
print(variable)

class_variable= one_hot_multiBin.classes_
print(class_variable)

# Now we are going to create our own tagger. 
     # This is for what? The answer is we may go through complicate English words sometimes (example: In medical terminologies). 
     # POS is a pre-trained and for a simple solution only. We couldn’t say it is not that much account. 
     # For the sake - We can train our own tagger (unlike the pre-trained pos tag package). 
     # But for this we need large corpus of texts. Here we going to download ‘brown’ package from corpus. 
     # Brown package is nothing but it already defined the large amount of pre-loaded texts with tags. 
     # So that we can use ‘back of taggers’ to train to create our own tagger to find out the accuracy of the same. 
     # Under the ‘back of taggers’ (back of n_grams) – we use three types of taggers. That are Unigram, Bigram & Trigram. 
         # Trigram checks that whether it can provide the tags for the given two words. If this condition fails to provide the expected – next it will go to Bigram. 
         # Bigram checks that whether it can provide the tags for the previous words. If this condition even fails to provides the expected – next it will go to Unigram. 
         # Unigram will finally check it to provide the tagger. 

# Import Library and download data. 
 
Brownie = nltk.download('brown')
print(Brownie)    # Verified that it's up-to-date. 

# Load Library. 

from nltk.corpus import brown
from nltk.tag import TrigramTagger
from nltk.tag import BigramTagger
from nltk.tag import UnigramTagger

# Get some text from the Brown Corpus, broken into sentences. 
sentences = brown.tagged_sents(categories='news')
print(sentences)  # Just for our references to see. 

# Split into 4000 sentences for traning and 623 for testing. 
train = sentences[:4000]
test = sentences[4000:]
# Create Backoff tagger
Unigram = UnigramTagger(train)
Bigram = BigramTagger(train, backoff=Unigram)
Trigram =TrigramTagger(train, backoff= Bigram)

# Show accuracy: 
Accuracy = Trigram.evaluate(test)
print(Accuracy)


# Notes:
    #  There in the line 19, you can see that 'pos_tag' is always alonged with 'word_tokenize'. 
    # Understand the code concept in the line 36, most importantly line 55 to 57. 