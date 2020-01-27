Created on Sun Jan 26 16:54:16 2020

@author: Manoj Saini
"""
# importing the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# importing the dataset
data  = pd.read_csv('D:\Python Work\dataset\Restaurant_Reviews.tsv', sep = '\t',quoting = 3, engine = 'python')  

# cleaing the texts
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

review = re.sub('[^a-zA-Z]', ' ',data['Review'][0]) 
review = review.lower()
review = review.split()
reveiw = [word for word in review if not word in set(stopwords.words('english'))] 
