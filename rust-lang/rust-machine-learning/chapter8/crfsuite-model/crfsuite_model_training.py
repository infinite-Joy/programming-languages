# coding: utf-8
from crfsuite_model import CRFSuiteModel
model = CRFSuiteModel("model.crfsuite")
res = model.fit("/Users/joydeepbhattacharjee/thinking/programming-languages/rust-lang/rust-machine-learning/chapter8/crfsuite-model/data/ner.csv")
print(res)
