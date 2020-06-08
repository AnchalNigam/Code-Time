import xlsxwriter
workbook = xlsxwriter.Workbook('/home/dell/Music/Example.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write(1, 0, 'hii anchal')
