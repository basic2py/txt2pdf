# txtdir2pdf.py        - text directory to pdf file                           |
#                                                                             |
#      see directory(s): /base/py.pvx/                                        |
#                      : /usr/local/lib/python3.6/site-packages/              |
#                      : /usr/local/lib64/python3.6/site-packages/            |
# pip3 install fpdf                                                           |
#                                                                             |
# python3 txtdir2pdf.py /home/pp/txt/ DOC.pdf
#                       sys.argv[1]   sys.argv[2]

import os, sys

num_arg = len(sys.argv)
if num_arg != 3: 
    print("usage: python3 txtdir2pdf.py /directory/txt_files/ /pdf/output.pdf")
    exit()

from fpdf import FPDF

def createPage(pdf):
    pdf.add_page()
    pdf.set_font('Courier', 'B', 8)   # 'Arial'

def printLine(pdf,ci,ln,lc,ml,dl,linetopr):
    cn = ci                      # character number
    for c2 in linetopr:
         pdf.text(cn , ln ,  c2 )
         cn += 2.2               # char size
    ln += 3; lc += 1             # line size control(s)
    if lc == ml:
        createPage(pdf)
        lc = 0; ln = dl
    return pdf,ci,ln,lc,ml,dl

files = []; fcnt  = 0; directory = sys.argv[1]  #   '/txt/'
for filename in os.listdir(directory):
    if filename.endswith(".TXT") or filename.endswith(".txt"):
        files.append(filename); fcnt=fcnt+1
    else:
        continue
files.sort()             # print(files); print(fcnt)

# create PDF file from all .txt and .TXT files in 'directory'
pdf = FPDF()             # pdf
dl, ml, ci = 10, 88, 12  # down lines, maximum lines on page, indent posr
ncl = 90                 # number of char on line

for filename in files:
    createPage(pdf)
    name = directory + "/" + filename
    file2 = open(name,"r")
    data2 = file2.readlines()
    file2.close()
    ln = dl
    lc = 0
    for line2 in data2:
        linetodo = line2
        while len(linetodo) > ncl-1:
            linetopr = linetodo[0:ncl]
            pdf,ci,ln,lc,ml,dl = printLine(pdf,ci,ln,lc,ml,dl,linetopr)
            linetodo = linetodo[ncl:]

        linetopr = linetodo
        pdf,ci,ln,lc,ml,dl = printLine(pdf,ci,ln,lc,ml,dl,linetopr)

pdf.output(sys.argv[2], 'F')
