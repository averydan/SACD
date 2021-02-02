import csv
import os
import sys
year = sys.argv[1]
if os.path.exists('./Output/schoolgrade' + str(year) +'_revised.csv'):
    os.remove('./Output/schoolgrade' + str(year) +'_revised.csv')
if os.path.exists('./Output/' + str(year) +'_schoolgrade_error_log.csv'):
    os.remove('./Output/' + str(year) +'_schoolgrade_error_log.csv')
with open('./Output/schoolgrade_revised' + str(year) +'.csv', 'r') as grad, open('./Resources/combined_poverty_rate_revised.csv', 'r') as poverty, open('./Output/schoolgrade' + str(year) +'_revised.csv', 'w') as out, open('./Output/' + str(year) +'_schoolgrade_error_log.csv', 'w') as log:
    writer = csv.writer(out)
    errorLogger = csv.writer(log)
    addedValue = False
    for rowGrad in csv.reader(grad):
        for rowPoverty in csv.reader(poverty):
            if rowGrad[1] == rowPoverty[0]:
                writer.writerow(rowGrad)
                addedValue = True
        if not addedValue:
            errorLogger.writerow(rowGrad)
        addedValue = False
        poverty.seek(0)