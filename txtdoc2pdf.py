# txtdoc2pdf.py        - text directory documentation to pdf file             |
#                                                                             |
#      see directory(s): /base/py.pvx/                                        |
#                      : /usr/local/lib/python3.6/site-packages/              |
#                      : /usr/local/lib64/python3.6/site-packages/            |
# pip3 install fpdf                                                           |
#                                                                             |
# python3 txtdoc2pdf.py /home/pp/txt/ DOC.pdf                                 |
#                       sys.argv[1]   sys.argv[2]                             |
import sys

num_arg = len(sys.argv)
if num_arg != 3: 
    print("usage: python3 txtdoc2pdf.py /directory/txt_files/ /pdf/output.pdf")
    exit()

from fpdf import FPDF
from txtflg2pdf import FLAGPDF, createPage, printLine, formatLine
from txtflg2pdf import pdfHeader, pdfFooter, chapterTitle
# get files to do
files = []
fcnt  = 0
directory = sys.argv[1]  #   '/txt/'
for filename in os.listdir(directory):
    if filename.endswith(".TXT") or filename.endswith(".KEY"):
        files.append(filename); fcnt=fcnt+1
    else:
        continue
files.sort()             # print(files); print(fcnt)

# create PDF file from all .txt and .TXT files in 'directory'
pdf = FPDF(orientation='P', unit='mm', format='A4')             # pdf
fz  = FLAGPDF()          # flags for pdf

# Table of Content - ToC - Files Links - Dummy load ---------------- start - | 
#
fz.title = fz.fd_title
pdf.add_page()

pdfHeader(pdf, fz)
num = '1 : Table of Content'
title = 'Files Links'
chapterTitle(pdf, fz, num, title)

fz.toc_link = pdf.add_link()
pdf.set_link(fz.toc_link )

pdf.set_font('Arial', '', 10 )
toc_y = fz.ln
x = 10 ; y = toc_y ; w = y ; h = 10   # h=0  w = x*y
fcnt  = 0
for filename in files:
    txt = '<' + filename + '>      '
    fz.curr_link = pdf.add_link()
    fz.file_link.append(fz.curr_link)
    fz.file_page.append('')                         # place holder 
    pdf.set_xy(x,y)
    pdf.cell(y, h, txt, link=fz.file_link[fcnt])
    fcnt += 1
    y=y+5 ; w = y
    if y > 225 :
        if x == 10:
            x = 65 ; y = toc_y  ; w = y
        else: 
            x =110 ; y = toc_y  ; w = y

# pdfFooter(pdf, fz)
#
# ------------------------------------------------------------------  end  - |
#                                                                            |
fcnt  = 0
#                                                                            |
# file layouts with link back to ToC on 'File Documention'---------- start - |
#
for filename in files:
    fz.cp = False           # control page - add a new page
    name2 = directory + "/" + filename
    file2 = open(name2,"r")
    data2 = file2.readlines()
    file2.close()
    fz.ln = fz.downlines
    fz.lc = 0
    fz.header= []
    fz.filehd= ''
    fz.dots = ''
    fz.num = str(pdf.page_no()+1)
    fz.name = filename
    fz.curr_fcnt = fcnt
    createPage(pdf, fz)
    fz.file_page[fcnt] = fz.num

    for line2 in data2:
        linetodo = line2
        while len(linetodo) > fz.ncl-1:
            linetopr = linetodo[0:fz.ncl]
            linetopr = formatLine(fz, linetopr)
            if len(linetopr) >0:
                printLine(pdf, fz, linetopr)
            if fz.addLine == 1 and fz.cp == False:
                linetopr = ' '
                printLine(pdf, fz, linetopr)
            linetodo = linetodo[fz.ncl:]

        linetopr = linetodo
        linetopr = formatLine(fz, linetopr)
        if len(linetopr) >0:
            printLine(pdf, fz, linetopr)
        if fz.addLine == 1 and fz.cp == False:
            linetopr = ' '
            printLine(pdf, fz, linetopr)
    #
    # if fz.lc < ( fz.ml - 11 ):  pdfFooter(pdf, fz)
    fcnt += 1
# ------------------------------------------------------------------  end  - |
#
#
# Table of Content - ToC - ----------- - load page numbers --------- start - | 
fz.curr_page = pdf.pages[1]
fcnt  = 0
for filename in files:
    txt1 = '<' + filename + '>      '                        # dummy load
    txt2 = fz.file_page[fcnt]+ ' : ' + filename              # load page number
    fz.curr_page = fz.curr_page.replace(txt1,txt2)
    fcnt += 1
pdf.pages[1] = fz.curr_page
# ------------------------------------------------------------------  end  - |
#                                                                            |
pdf.output(sys.argv[2], 'F')
