# csv2xlsx.py          - csv file to xlsx file   - `python.pxp`  - centos 7   |
#                                                                             |
#      see directory(s): /base/py.pvx/                                        |
#                      : /usr/local/lib/python3.6/site-packages/              |
#                      : /usr/local/lib64/python3.6/site-packages/            |
# pip3 install pandas                                                         |
# pip3 install openpyxl                                                       |
#                                                                             |
# the cvs input file, records MUST all have the same number of commas on each |
# line.                                                                       |
#                                                                             |
# python3 csv2xlsx.py /var/www/html/bk/download/mm_sn/gltb.csv                |
#                     sys.argv[1]                              - (input file) |
#                     /var/www/html/bk/download/mm_sn/gltb.xlsx               |
#                     sys.argv[2]                              - (output)     |
import sys

num_arg = len(sys.argv)
if num_arg != 3:
    print("usage: python3 csv2xlsx.py /input/file.csv /output/file.xlsx")
    exit()

import pandas as pd 

# Reading the csv file 
df = pd.read_csv(sys.argv[1]) 
  
# saving xlsx file 
xl = pd.ExcelWriter(sys.argv[2])
df.to_excel(xl, index = False) 
  
xl.save() 
