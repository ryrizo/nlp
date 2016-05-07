#splitter
from sklearn.datasets import load_svmlight_files
trn_X, trn_y, tst_X, tst_y = load_svmlight_files(("C:/Users/Ryan/git/nlp/trn.dat", "C:/Users/Ryan/git/nlp/tst.dat"))
print trn_X.shape[1]