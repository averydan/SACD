import csv
import sys
import os
total = 0
otherTotal = 0
year = sys.argv[1]
if os.path.exists('./Output/cleanschooldemographics' + str(year) +'_name_match.csv'):
    os.remove('./Output/cleanschooldemographics' + str(year) +'_name_match.csv')
addedValue = False
with open('./Resources/cleanschooldemographics' + str(year) +'.csv', 'r') as grad, open('./Output/cleanschooldemographics2019_revised.csv', 'r') as corpId, open('./Output/cleanschooldemographics' + str(year) +'_name_match.csv', 'w') as out:
    writer = csv.writer(out)
    for rowGrad in csv.reader(grad):
        for rowCorpId in csv.reader(corpId):
            if rowGrad[0] == rowCorpId[0]:
                tempDict = rowGrad
                tempDict[1] = rowCorpId[1]
                writer.writerow(tempDict)
                addedValue = True
                total += 1
        if not addedValue:
            writer.writerow(rowGrad)
            otherTotal += 1
        addedValue = False
        corpId.seek(0)
    print('Matches:')
    print(total)
    print('Non Matches:')
    print(otherTotal)