#-*- coding: utf8 -*-
import sys
import time
import traceback
import os,time
import random
import xlrd


class Exceldiff(object):
    "C:\Python34\Scripts ./pip.exe install xlrd "
    file1 = 'checklist-app-2015-12-01.xls'
    file2 = 'checklist-app-2015-12-09.xls'

    def get_files(self):
        self.data1 = xlrd.open_workbook(self.file1)
        self.data2 = xlrd.open_workbook(self.file2)

    def excel_diff(self):
        
        table1 = self.data1.sheet_by_index(0)
        table2 = self.data2.sheet_by_index(0)

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

    def main(self):
        self.get_files()
        self.excel_diff()
            
if __name__ == '__main__':

    myDiff = Exceldiff()
    myDiff.main()
