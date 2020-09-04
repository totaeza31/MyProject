import spacy
from spacy.lang.pt.stop_words import STOP_WORDS
from sklearn.feature_extraction.text import CountVectorizer
import pt_core_news_sm
import deepcut
import csv
from progress.bar import IncrementalBar


# from progress.bar import Bar

# bar = Bar('Processing', max=20000000000000000000000000)
# for i in range(100000000000000000000000000000000000000000):
#     # Do some work
#     bar.next()
# bar.finish()


def opendatacsv():
 with open('./testCode/csv/raikan_ahan.csv', encoding="utf8") as csvfile:
  test = csv.reader(csvfile)
  header = next(test)
  nlp = pt_core_news_sm.load()
  allcomment = []
  ii=0
  data = list(test)
  row_count = len(data)
  print(row_count)
  max = 2000
  bar = IncrementalBar(f'Word segment file ',max = max ,suffix='%(percent)d%% %(elapsed_td)s')
  for row in test:
   words=row[0]

   doc = nlp(words)
   corpus = [sent.text.lower() for sent in doc.sents ]
   cv = CountVectorizer(stop_words=list(STOP_WORDS))   
   cv_fit=cv.fit_transform(corpus)    
   word_list = cv.get_feature_names();    
   count_list = cv_fit.toarray().sum(axis=0)
   word_frequency = dict(zip(word_list,count_list))

   val=sorted(word_frequency.values())
   higher_word_frequencies = [word for word,freq in word_frequency.items() if freq in val[-3:]]
#   print("\nWords with higher frequencies: ", higher_word_frequencies)

# gets relative frequency of words
   higher_frequency = val[-1]
   for word in word_frequency.keys():  
     word_frequency[word] = (word_frequency[word]/higher_frequency)

   sentence_rank={}
   for sent in doc.sents:
     for word in sent :       
        if word.text.lower() in word_frequency.keys():            
            if sent in sentence_rank.keys():
                sentence_rank[sent]+=word_frequency[word.text.lower()]
            else:
                sentence_rank[sent]=word_frequency[word.text.lower()]
   top_sentences=(sorted(sentence_rank.values())[::-1])
   top_sent=top_sentences[:2]

   summary=[]
   for sent,strength in sentence_rank.items():  
    if strength in top_sent:
        summary.append(sent)
    else:
        continue

   
   keepSummarizeword =  []
   for i in summary:
     
     replacedot = str(i)
     replaces = replacedot.replace(".","")
     allcomment.append(replaces)    
     ii+=1
    #  print("counts >> ",ii)
     bar.next()
#   print(allcomment)
 bar.finish()  
 return allcomment

opendatacsv()