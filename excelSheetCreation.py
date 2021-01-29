from openpyxl import Workbook

i=2
symbol=input("Enter the symbol to differentiate: ")
filename=input('Enter the filename/location of your text file: ')

wb=Workbook()
sheet=wb['Sheet']
with open(filename) as f:
    for line in f:
        datas=line.split(symbol)
        
        if datas[0]=='\n':
            continue
        sheet['A'+str(i)]=datas[0]
        sheet['B'+str(i)]=datas[1]
        sheet['C'+str(i)]=datas[2]
        sheet['D'+str(i)]=datas[3]
        sheet['E'+str(i)]=datas[4]
        sheet['F'+str(i)]=datas[5]
        sheet['G'+str(i)]=datas[6].rstrip()
        i=i+1

       

wb.save('chandamSinhaSirProject.xlsx')
print("ASSIGNMENT COMPLETED")
            
