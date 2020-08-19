def DeepcutandTLTK():

        valuesDeepcutandTLTK = []   
        text = "ทดสอบการตัดคำ"
# cut word 
        list_word = deepcut.tokenize(text)
# POS 
        i = tltk.nlp.pos_tag(list_word)
        changeListToString = str(i)
# clean
        clean3 = changeListToString.replace("(',', 'PUNCT'),", "") \
                      .replace(", ('<s/>', 'PUNCT')", "")\
                      .replace("('[', 'SYM'),", "")\
                      .replace(", (']', 'SYM')", "")\
                      .replace("  ", "")\
                      .replace(", (',.]', 'ADV'),","")
       
        valuesDeepcutandTLTK.append(clean3)      
        return valuesDeepcutandTLTK

def DeepcutandPythai():

        valuesDeepcutandPythai = []   
        text= "ทดสอบการตัดคำ"
        list_word = deepcut.tokenize(text)
        senten = pos_tag(list_word, corpus='orchid_ud')
        tests = [senten]
        test = str(tests)

        clean = test.replace(", (' ', 'PUNCT'), ", "],[")
        clean2 = clean.replace(" ", "")
        valuesDeepcutandPythai.append(clean2)
     
        return valuesDeepcutandTLTK