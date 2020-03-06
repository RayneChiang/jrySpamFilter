import jieba
import jieba.analyse
import os
import re
import pandas as pd
import _thread
import time


class generateEmail:

    def __init__(self,content):
        self.spamCol = ["Word", "Frequency"]
        self.content = content

    def generate(self):
        module_path = os.path.dirname(__file__)

        spamWord = module_path + "/spamWords.csv"
        normalWord = module_path + "/normalWords.csv"

        if self.content == "spam":

            spamfile = module_path + "/data/spam/"
            spamWrite = module_path +"/data/spamFrequency.csv"

        else:

            spamfile = module_path + "/data/normal/"
            spamWrite = module_path +"/data/normalFrequency.csv"

        spamDictionary = pd.read_csv(spamWord)
        normalDictionary = pd.read_csv(normalWord)

        spamFrequencyList = []


        spamDictionary.columns = ['index', 'Word', 'Frequency']
        normalDictionary.columns = ['index','Word','Frequency']

        for i in range(1, 8000):
            wordList = []

            spamProSum = 0
            normalProSum = 0

            judge = 0

            file = spamfile + str(i) + ""

            try:
                tempSpam = open(file)
                spam = tempSpam.read()

            except FileNotFoundError:
                i = i + 1

            spam = re.sub("[A-Za-z0-9\!\%\[\]\,\。\.\-\#\&\_]", "", spam)

            tag = jieba.analyse.extract_tags(spam, 10, True)

            tempSpam.close()

            for n in tag:
                wordList.append(n)
            pass

            tagList = pd.DataFrame(columns=self.spamCol, data=wordList)

            for index, row in tagList.iterrows():
                varFrequency = row['Frequency']
                varWord = row['Word']
                dataSpam = spamDictionary[spamDictionary['Word'] == varWord]
                dataNormal =normalDictionary[normalDictionary['Word'] ==varWord]

                spamPro = 0
                normalPro = 0

                if not dataSpam.empty:
                    dicFrequency = float(dataSpam['Frequency'])
                    spamPro = dicFrequency * varFrequency
                    spamProSum = spamProSum + spamPro
                pass

                if not dataNormal.empty:
                    dicFrequency = float(dataNormal['Frequency'])
                    normalPro = dicFrequency * varFrequency
                    normalProSum = normalProSum + normalPro
                pass
            pass

            count = 0
            if  spamProSum > normalProSum:
                judge = 1
                count = count+1

            tempdata = [i, spamProSum,normalProSum,judge]

            spamFrequencyList.append(tempdata)
            pass
            print(str(i)+self.content)
        pass

        wordcol = ['emailNumber', 'spam Probability', 'normal Probability ', 'judge']
        wList = pd.DataFrame(columns=wordcol, data=spamFrequencyList)

        print (count)
        wList.to_csv(spamWrite)

    pass


pass


def main():

    generateEmail(content='normal').generate()
    print("normal judge has been created")
    #
    generateEmail(content='spam').generate()
    print("spam judge has been created")


if __name__ == '__main__':
    main()
