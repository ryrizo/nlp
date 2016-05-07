import math
import sys
from tokenizer import getTokenList

def tfidf_main(sys_arg_1, sys_arg_2):
    input = open(sys_arg_1, "r")
    totdocs = int(input.readline().strip("\r\n"))
    termList = []
    idf = dict()
    for line in input:
        value = line.strip("\r\n").split("\t")
        termList.append(value[0])
        idf[value[0]] = math.log(1.0 * totdocs / int(value[1]))
    input.close()

    for line in open(sys_arg_2, "r"):
        value = line.strip("\r\n").split("\t")
        id = value[0]
        labels = value[1]
        title = value[2]
        body = value[3]
        tf = dict()
        for ngram in getTokenList(title):
            if (ngram in tf):
                tf[ngram] = tf[ngram] + 1
            else:
                tf[ngram] = 1
        for ngram in getTokenList(body):
            if (ngram in tf):
                tf[ngram] = tf[ngram] + 1
            else:
                tf[ngram] = 1
        label = "-1"
        if ("acq" in labels):
            label = "1" 
        tfidf = dict()
        norm = 0.0
        for ngram in tf:
            if (ngram in idf):
                tfidf[ngram] = tf[ngram] * idf[ngram]
                norm = norm + (tfidf[ngram] ** 2)
        norm = math.sqrt(norm)
        assignmentList = []
        index = 1
        for ngram in termList:
            if (ngram in tfidf):
                assignmentList.append(str(index) + ":" + str(tfidf[ngram] / norm))
            index = index + 1
        print(label + " " + " ".join(assignmentList))

if __name__ == '__main__':
    tfidf_main(sys.argv[1], sys.argv[2])