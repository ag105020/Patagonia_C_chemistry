'''
Created on May 18, 2014

@author: Keisuke
'''
from pylab import * 

def st(parameter,savefolder,name):
    First_part="C:\\Users\\keiin\\OneDrive\\Desktop\\figures\\02\\10 Patagonia\\"
    Second_part=savefolder+"\\"+name
    Last_part=".csv"
    savetxt(First_part+Second_part+Last_part, parameter, delimiter=",",fmt="%s")