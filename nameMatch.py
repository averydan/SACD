import csv
import sys
import os
total = 0
otherTotal = 0
year = sys.argv[1]
if os.path.exists('./Output/schoolgrade_revised' + str(year) +'.csv'):
    os.remove('./Output/schoolgrade_revised' + str(year) +'.csv')
addedValue = False
with open('./Resources/schoolgrade' + str(year) +'.csv', 'r') as grad, open('./Resources/guide.csv', 'r') as corpId, open('./Output/schoolgrade_revised' + str(year) +'.csv', 'w') as out:
    writer = csv.writer(out)
    for rowGrad in csv.reader(grad):
        for rowCorpId in csv.reader(corpId):
            if rowGrad[0] == rowCorpId[0]:
                writer.writerow([rowCorpId[0],rowCorpId[1],rowGrad[2]])
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



