import datetime
import xlsxwriter


f = open("./oneM2MTester.ubuntu-mtc.log", 'r')

workbook = xlsxwriter.Workbook('testing_result.xlsx')
worksheet = workbook.add_worksheet()
excelIndex = 1;

for index in range(120):
    line = f.readline()

    start_time = ""
    end_time = ""

    if index % 2 == 0:
        start_time = line[12:24]
    elif index % 2 == 1:
        end_time = line[12:24]

    excelIndexA = 'A' + str(excelIndex);
    excelIndexB = 'B' + str(excelIndex);

    print(excelIndex)
    print(excelIndexA)
    print(excelIndexB)
    worksheet.write(excelIndexA, start_time)
    worksheet.write(excelIndexB, end_time)

    if index % 2 == 1:
        excelIndex += 1

workbook.close()

f.close()