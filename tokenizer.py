#!/usr/bin/python

import re
import sys
from nltk.tokenize import wordpunct_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

stopSet = set(stopwords.words("english"))
stemmer = PorterStemmer()
alphanumeric = re.compile("^[0-9A-Za-z]+$")

def getTokenList(text,
                 lowercaseTokensRequested = True,
                 stopwordRemovalRequested = True,
                 stemmedTokensRequested = True,
                 symbolicTokenRemovalRequested = True,
                 ngramMaxLength = 1):
    text = re.sub("[\s\r\n]+", " ", text)    # collapse whitespace
    if (lowercaseTokensRequested):
        text = text.lower()    # lowercase line
    tokenList = []
    for token in wordpunct_tokenize(text):
        if (stopwordRemovalRequested and (token in stopSet)):
            token = ""    # remove stopword
        else:
            if (stemmedTokensRequested):
                token = stemmer.stem(token)    # stem the token
            if (symbolicTokenRemovalRequested and (not alphanumeric.match(token))):
                token = ""    # remove symbolic token
        tokenList.append(token)
    ngramList = []
    tokenListLength = len(tokenList)
    for i in range(tokenListLength):
        if (len(tokenList[i]) > 0):
            ngram = ""
            for j in range(ngramMaxLength):
                if ((i + j) < tokenListLength):
                    token = tokenList[i + j]
                    if (len(token) == 0):
                        break
                    else:
                        if (j == 0):
                            ngram = token
                        else:
                            ngram = ngram + "_" + token
                        ngramList.append(ngram)
    return ngramList
