# coding: utf-8
from crfsuite_model import CRFSuiteModel
model = CRFSuiteModel("model.crfsuite")
res = model.predict("/Users/joydeepbhattacharjee/thinking/programming-languages/rust-lang/rust-machine-learning/chapter8/crfsuite-model/data/ner_predict.csv")
print(res)
