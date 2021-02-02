import csv
import os
import sys
total = 0
year = sys.argv[1]
if os.path.exists('./Output/cleanschooldemographics' + str(year) +'_revised.csv'):
    os.remove('./Output/cleanschooldemographics' + str(year) +'_revised.csv')
if os.path.exists('./Output/cleanschooldemographics' + str(year) +'_error_log.csv'):
    os.remove('./Output/cleanschooldemographics' + str(year) +'_error_log.csv')
with open('./Output/cleanschooldemographics' + str(year) +'_name_match.csv', 'r') as grad, open('./Resources/combined_poverty_rate_revised.csv', 'r') as poverty, open('./Output/cleanschooldemographics' + str(year) +'_revised.csv', 'w') as out, open('./Output/cleanschooldemographics' + str(year) +'_error_log.csv', 'w') as log:
    writer = csv.writer(out)
    errorLogger = csv.writer(log)
    addedValue = False
    for rowGrad in csv.reader(grad):
        for rowPoverty in csv.reader(poverty):
            if rowGrad[1] == rowPoverty[0]:
                writer.writerow(rowGrad)
                addedValue = True
                total += 1
        if not addedValue:
            errorLogger.writerow(rowGrad)
        addedValue = False
        poverty.seek(0)
    print(total)