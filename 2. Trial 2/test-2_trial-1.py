#import the libraries
from tokenize import Name
import pandas as pd
import re
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import csr_matrix
import sparse_dot_topn.sparse_dot_topn as ct
import time

pd.set_option('display.max_colwidth', -1)

#load the data
data = pd.read_csv('room_type.csv')

#printinf first 5 rows
print("=======================printing the data==================\n")
print(data.head(5))
print("==========================================================\n")

#creating N-gram part
def ngram(string, n = 3):
    string = re.sub(r'[,-./]|\sBD',r'',string)
    ngrams = zip(*[string[i:] for i in range(n)])
    return [''.join(ngram) for ngram in ngrams]

#testing ngrams work for verification
print("======================printing the ngram==================\n")
print('All 3-grams in "Rohan" : ',ngram('Rohan'))
print("==========================================================\n")

#TF-IDF featurs using Tfidfvectorize by Scikit-Learn library
name = data['RoomTypes']
vectorizer = TfidfVectorizer(min_df=1, analyzer=ngram)
tf_idf_matrix = vectorizer.fit_transform(name)
print("====================printing the TF-IDF===================\n")
print(tf_idf_matrix[0])
print("==========================================================\n")

#We are dealing with a CSR matrix with sparse_dot_topn library.
def top10(A, B, ntop, lower_bound = 0):
    #A and B as a CSR matrix.
    A = A.tocsr()
    B = B.tocsr()
    M, _ = A.shape
    _, N = B.shape

    idx_dtype = np.int32
    nnz_max = M*ntop

    indptr = np.zeros(M+1, dtype = idx_dtype)
    indices = np.zeros(nnz_max, dtype = idx_dtype)
    data = np.zeros(nnz_max, dtype=A.dtype)

    ct.sparse_dot_topn(
        M, N, np.asarray(A.indptr, dtype = idx_dtype),
        np.asarray(A.indices, dtype=idx_dtype),
        A.data,
        np.asarray(B.indptr, dtype = idx_dtype),
        np.asarray(B.indices, dtype = idx_dtype),
        B.data,
        ntop,
        lower_bound,
        indptr, indices, data
    )
    return csr_matrix((data,indices,indptr),shape=(M,N))

#  Top 10 with similarity above 0.8
t1 = time.time()
matches = top10(tf_idf_matrix, tf_idf_matrix.transpose(), 10, 0.8)
t = time.time()-t1
print("Time taken by item with similarity >= 0.8 is :", t)
print("==========================================================\n")


#unpacking the resulting sparse matrix
def get_matches_df(sparse_matrix, name_vector, top = 100):
    non_zeros = sparse_matrix.nonzero()

    sparserows = non_zeros[0]
    sparsecols = non_zeros[1]

    if top:
        nr_matches = top
    else:
        nr_matches = sparsecols.size
    
    left_side = np.empty([nr_matches], dtype=object)
    right_side = np.empty([nr_matches], dtype=object)
    similairity = np.zeros(nr_matches)
    
    for index in range(0, nr_matches):
        left_side[index] = name_vector[sparserows[index]]
        right_side[index] = name_vector[sparsecols[index]]
        similairity[index] = sparse_matrix.data[index]
    
    return pd.DataFrame({'left_side': left_side,
                          'right_side': right_side,
                           'similairity': similairity})

#store the matches into new dataframe called matched-data and
#printing 5 samples

matched_data = get_matches_df(matches, name, top=200)
matched_data = matched_data[matched_data['similairity'] < 0.99999] # For removing all exact matches
print(matched_data.sample(5))

#printing the matches in sorted order
matched_data.sort_values(['similairity'],ascending = False).head(10)

print("File is saved as similairity.csv")

matched_data.to_csv('similairity.csv')