# C:\Python34\Scripts ./pip.exe install xlrd
import xlrd
data1 = xlrd.open_workbook('checklist-app-2015-12-01.xls')
data2 = xlrd.open_workbook('checklist-app-2015-12-09.xls')

table1 = data1.sheet_by_index(0)
table2 = data2.sheet_by_index(0)

nrows = table1.nrows

#get the columb values
lst1= list(set(table1.col_values(2)))
lst2= list(set(table2.col_values(3)))

lst1 = sorted(lst1)
lst2 = sorted(lst2)

print ("1.xls is :")
print ("---"*10)
for i in range(len(lst1) ):
    print (lst1[i])
print ("Total number:%d"%len(lst1))

print ("2.xls is :")
print ("---"*10)
for i in range(len(lst2) ):
    print (lst2[i])
print ("Total number:%d"%len(lst2))
    
print ("---"*10)
print ("Difference is :")
print ("---"*10)

dif_list = list(set(lst2).difference(set(lst1)))
for i in range(len(dif_list) ):
    print (dif_list[i])


print ("---"*10)
print ("Total number:%d"%len(dif_list))
