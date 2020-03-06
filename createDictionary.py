import jieba
import jieba.analyse
import os
import re
import pandas as pd
import numpy as np


class createDictionary:

    def __init__(self,content):
        self.spamCol = ["Word", "Frequency"]
        self.content = content

    def Dictionary(self):
        module_path = os.path.dirname(__file__)
        if self.content == "spam" :
            spamword = module_path+"/spamWords.csv"
            spamfile = module_path+"/data/spam/"
        else  :
            spamword = module_path+"/normalWords.csv"
            spamfile = module_path+"/data/normal/"


        wordlist=[]
        freqList=[]

        for i in range(1,6800):

            file = spamfile+str(i)+""

            try:
                spam = open(file).read()

            except FileNotFoundError:
                i = i+1

            spam = re.sub("[A-Za-z0-9\!\%\[\]\,\。\.\-\#\&\_]", "", spam)

            tag=jieba.analyse.extract_tags(spam,5,True)

            for n in tag:
                wordlist.append(n)
            pass

        pass



        df = pd.DataFrame(columns=self.spamCol, data=wordlist)

        words = np.unique(df['Word'])

        for w in words:
            data = df[df['Word'] == w]
            frequencySum = round(data['Freq uency'].sum(),2)
            tempdata = [w,frequencySum]
            freqList.append(tempdata)

        # freqlist is not callable
        def callableList(freqList):
            return freqList[1]

        freqList.sort(key=callableList)

        freqList.reverse()

        dList = pd.DataFrame(columns=self.spamCol,data=freqList)

        dList.to_csv(spamword)

        print(self.content + "Dictionary has been created")


def main():
    createDictionary(content="normal").Dictionary()

    createDictionary(content="spam").Dictionary()


if __name__ == '__main__':
    main()
















