# txt2pdf
text to pdf
umentat
in basic it was easy to create reports or csv files, i then needed to do a pdf or excel file from the report or csv file.
this is where python3 came into play. after some time looking, i just started to code what was needed.
the program outlines install(s) needed.

         txt2pdf.py - from one text file creates a pdf file.
python3 txt2pdf.py /directory/filename.txt  /directory/filename.pdf

        txtdir2pdf.py  - from a directory (all .txt and .TXT files) create a pdf file.
python3 txtdir2pdf.py /directory/txt_files/ /pdf/output.pdf

        txtdoc2pdf.py - from documentation directory create a pdf file with page links. (need txtflg2pdf.py for this program)
python3 txtdoc2pdf.py /directory/txt_files/ /pdf/output.pdf

        csv2xlsx.py - from csv create a xlsx file  
python3 csv2xlsx.py /input/file.csv /output/file.xlsx

