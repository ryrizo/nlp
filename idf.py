import sys
from tokenizer import getTokenList

def idf_main(min_doc_freq, read_file):
    minDocFreq = int(min_doc_freq)

    docfreq = dict()
    totdocs = 0
    for line in open(read_file, "r"):
        value = line.strip("\r\n").split("\t")
        id = value[0]
        labels = value[1]
        title = value[2]
        body = value[3]
        observed = set()
        for ngram in getTokenList(title):
            if (ngram not in observed):
                observed.add(ngram)
        for ngram in getTokenList(body):
            if (ngram not in observed):
                observed.add(ngram)
        for ngram in observed:
            if (ngram in docfreq):
                docfreq[ngram] = docfreq[ngram] + 1
            else:
                docfreq[ngram] = 1
        totdocs = totdocs + 1

    ngramList = []
    for ngram in docfreq:
        ngramList.append(ngram)
    ngramList.sort()

    print(str(totdocs))
    for ngram in ngramList:
        if (docfreq[ngram] >= minDocFreq):
            print(ngram + "\t" + str(docfreq[ngram]))

if __name__ == '__main__':
    idf_main(sys.argv[1],sys.argv[2])
