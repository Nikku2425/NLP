import spacy
nlp=spacy.load('en_core_web_sm')

doc=nlp("nikhil is erripuku, Anji is also an erripuku")

for word in doc:
  print(word," | ",word.pos_)
