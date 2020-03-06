import os
import pandas as pd

class rightCalculation:

    def cal(self):
        module_path = os.path.dirname(__file__)

        spamDir = module_path + "/data/spamFrequency.csv"
        normalDir = module_path + "/data/normalFrequency.csv"

        spamJudge = pd.read_csv(spamDir)
        spamNumber = spamJudge[spamJudge['judge'] == 1]
        spamCal = len(spamNumber) / len(spamJudge)

        print(spamCal)

        normalJudge = pd.read_csv(normalDir)
        normalNumber = normalJudge[normalJudge['judge'] == 0]
        normalCal = len(normalNumber) / len(normalJudge)

        print(normalCal)

    pass

pass



def main():
    rightCalculation().cal()

if __name__ == '__main__':
    main()