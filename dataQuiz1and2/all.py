import tltk
import csv
import deepcut
import pandas as pd
import time
import tltk
from pythainlp.tag import pos_tag


def DeepcutandTLTK():

        valuesDeepcutandTLTK = []   
        text = "ทดสอบตัวตัดคำ ssนะจ้ะdsdsd/*-"
# cut word 
        cleans1 = str(text)
        cleans = cleans1.translate({ord(c): "" for c in "\"'!@#$ %^&*,[](){};:./<>?|`~-=_+\\"})
        list_word = deepcut.tokenize(cleans)

        strlist_word = str(list_word)
        replaces =strlist_word.replace("[","") \
                              .replace("'","") \
                              .replace("]","") \
                              .replace(" ","")
                        
        pos = tltk.nlp.pos_tag(replaces)
        
        
# POS   Replace ใหม่อีกครั้งเพราะ เอาคำที่ตัดไปใช้ต่อใน tltk (tltk เอาคำที่ไม่ตัด[ข้อความปกติ]มาตัดด้วยก็เลยให้คั่นด้วย , จะได้ตัดของdeepcut )   
        strpos = str(pos)
        cleanPOS = strpos.replace("(',', 'PUNCT'), ", "") \
                         .replace("[[","[") \
                         .replace("]]","]")
        valuesDeepcutandTLTK.append(cleanPOS)      
        return valuesDeepcutandTLTK

def DeepcutandPythai():

        valuesDeepcutandPythai = []   
        text = "ทดสอบตัวตัดคำ ssนะจ้ะdsdsd/*-"
        cleans1 = str(text)
        cleans = cleans1.translate({ord(c): "" for c in "\"'!@#$ %^&*,[](){};:./<>?|`~-=_+\\"})

        list_word = deepcut.tokenize(cleans)
        senten = pos_tag(list_word, corpus='orchid_ud')
   
        valuesDeepcutandPythai.append(senten)
        return valuesDeepcutandPythai


# deepcut+tltk ["[('ทดสอบ', 'NOUN'), ('ตัว', 'NOUN'), ('ตัด', 'VERB'), ('คำ', 'NOUN'), (',ss,', 'PART'), ('นะ', 'NOUN'), ('จ้ะ', 'NOUN'), (',dsdsd', 'NOUN'), ('<s/>', 'PUNCT')]"]
# ["("] เเก้ไม่หาย

# deepcut+pythai [[('ทดสอบ', 'VERB'), ('ตัว', 'NOUN'), ('ตัด', 'VERB'), ('คำ', 'NOUN'), ('ss', 'NOUN'), ('นะ', 'NOUN'), ('จ้ะ', 'NOUN'), ('dsdsd', 'NOUN')]]

DeepcutandTLTK()
DeepcutandPythai()
