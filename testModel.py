import os
import re
import jieba
import jieba.analyse
import pandas as pd
import numpy as np


class testModel:

    def test(self):
        module_path = os.path.dirname(__file__)

        spamWord = module_path + "/spamWords.csv"
        normalWord = module_path + "/normalWords.csv"
        spamDictionary = pd.read_csv(spamWord)
        normalDictionary = pd.read_csv(normalWord)

        spamCol = ["Word", "Frequency"]

        wordList = []

        file = module_path + "/test.txt"

        test = open(file, encoding='GBK').read()

        test = re.sub("[A-Za-z0-9\!\%\[\]\,\。\.\-\#\&\_]", "", test)

        tag = jieba.analyse.extract_tags(test, 10, True)

        for n in tag:
            wordList.append(n)
        pass

        tagList = pd.DataFrame(columns=spamCol, data=wordList)

        spamFreSum = 0
        normalFreSum = 0

        for index, row in tagList.iterrows():
            varFrequency = row['Frequency']
            varWord = row['Word']
            dataSpam = spamDictionary[spamDictionary['Word'] == varWord]
            dataNormal = normalDictionary[normalDictionary['Word'] == varWord]

            spamPro = 0
            normalPro = 0

            if not dataSpam.empty:
                dicFrequency = float(dataSpam['Frequency'])
                spamPro = dicFrequency * varFrequency
                spamFreSum = spamFreSum + spamPro
            pass

            if not dataNormal.empty:
                dicFrequency = float(dataNormal['Frequency'])
                normalPro = dicFrequency * varFrequency
                normalFreSum = normalFreSum + normalPro
            pass
        pass

        if spamFreSum > normalFreSum:
            print("it is spam letter")
            return 1
        else:
            print("it is normal letter")
            return 0

    pass
pass


def main():
    testModel().test()


if __name__ == '__main__':
    main()
