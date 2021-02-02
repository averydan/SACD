import csv

with open('./Resources/2019_grad_rates_revised.csv', 'r') as grad, open('./Resources/combined_poverty_rate.csv', 'r') as poverty, open('./Resources/combined_poverty_rate_revised_test.csv', 'w') as out, open('./Resources/combined_poverty_rate_error_log_test.csv', 'w') as log:
    writer = csv.writer(out)
    errorLogger = csv.writer(log)
    addedValue = False
    for rowPoverty in csv.reader(poverty):
        for rowGrad in csv.reader(grad):
            if rowPoverty[0] == rowGrad[1]:
                writer.writerow(rowPoverty)
                addedValue = True
        if not addedValue:
            errorLogger.writerow(rowPoverty)
        addedValue = False
        grad.seek(0)




# with open('./Resources/2019_grad_rates_revised_copy.csv', 'r') as base, open('./Resources/combined_poverty_rate.csv', 'r') as inp, open('./Resources/combined_poverty_rate_revised.csv', 'w') as out, open('./Resources/combined_poverty_rate_error_log.csv', 'w') as log:
#     writer = csv.writer(out)
#     errorLogger = csv.writer(log)
#     addedValue = False
#     for rowInp in csv.reader(inp):
#         for rowBase in csv.reader(base):
#             if rowInp[1] == rowBase[0]:
#                 writer.writerow(rowInp)
#                 addedValue = True
#         if not addedValue:
#             errorLogger.writerow(rowInp)
#         addedValue = False
#         base.seek(0)