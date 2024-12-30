import xlsxwriter

workbook = xlsxwriter.Workbook('veri.xlsx')
worksheet = workbook.add_worksheet()

row = 0
col = 0

for row_data in StokTakip:
  worksheet.write(row, col, row_data.1)
  worksheet.write(row, col+1, row_data.2)
  worksheet.write(row, col+2, row_data.3)
  row += 1

workbook.close()