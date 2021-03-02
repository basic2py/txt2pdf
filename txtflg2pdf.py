# txtflg2pdf.py   - controls for PDF printing                                 |
#                                                                             |
#      see directory   : /base/py.pvx/                                        |
#                                                                             |
# this class used only in `txtdoc2pdf.py` flag controls for pdf stuff fz.     |
                                           
class FLAGPDF(object):

    def __init__(self, family='Courier',style='B',size=8):

        # Initialization of properties
        self.family=family
        self.style=style
        self.size=size

        # if size == 8:
        self.v_cn = 2.2              # char size control
        self.v_ln = 3.0              # line size control   

        self.downlines = 2           # down number of lines
        self.ml = 88                 # number of lines on page (80)
        self.ci = 12                 # char indent position
        self.ncl = 90                # number of char on line

        self.ln = 0.0                # line position 
        self.lc = 0                  # line counter
        self.cp = False              # control page - add a new page

        self.fd_title = 'File Documention'
        self.name = ''
        self.header = []
        self.filehd = ''               # Continued on next page(s)
        self.cont = 'Continued'
        self.title  = self.fd_title
        self.dot    = '.'
        self.dots   = ''
        self.toc_link = ''
        self.curr_link = ''

        self.file_link = []
        self.file_page = []
        self.last_page = 0
        self.curr_page = ''
        self.curr_fcnt = ''
        self.addLine  = 0

def createPage(self, fz):
    self.add_page()
    fz.cp = False
    self.set_font(fz.family, fz.style, fz.size )
    pdfHeader(self, fz)

    if fz.addLine == 1 and fz.cp == False:
        linetopr = ' '
        printLine(self, fz, linetopr)

    if fz.filehd == '':
        num = fz.num
        title = fz.name 
        chapterTitle(self, fz, num, title)    
        self.set_link(fz.file_link[fz.curr_fcnt])

#    if fz.filehd != '':
#        fz.header= []
#        fz.header.append(fz.filehd + '                                     ' + fz.cont + fz.dots )
#        fz.header.append(' ')
#        fz.dots += fz.dot

 #   for line1 in fz.header:
 #       linetopr = line1 
 #       printLine(self, fz, linetopr)

def pdfHeader(self, fz):
    self.set_font('Arial', 'B', fz.size + 2)            # Arial bold 15
    w = self.get_string_width(fz.title) + 6       # Cal width of title & pos
    self.set_x((210 - w) / 2)
    self.set_draw_color(0, 80, 180)       # Colors of frame, BG and text
    self.set_fill_color(200, 220, 255)
    self.set_text_color(128)                   # Text color in gray
    self.set_line_width(1)                     # Thickness of frame (1 mm)
    self.cell(w, 8, fz.title, 1, 1, 'C', 1, fz.toc_link )      # Title was 9
    self.ln(4)                                # Line break 10
    self.set_font(fz.family, fz.style, fz.size )
    self.set_text_color(128)                   # Text color in gray
    fz.ln = fz.ln + (fz.v_ln * 8) ; fz.lc += 8 # line size control(s)

def pdfFooter(self, fz):
    # self.set_y(-33)                   # Position at 1.5 cm from bottom -33
    x = 0; y = 260
    self.set_xy(x,y)
    self.set_font('Arial', 'I', fz.size + 2)            # Arial italic 8
    self.set_text_color(128)                   # Text color in gray
    txt = ' - ' + str(self.page_no()) +  ' - '
    self.cell(0, 8, txt, 0, 0, 'C', 0, fz.toc_link ) # was 10
    self.set_font(fz.family, fz.style, fz.size )
    self.set_text_color(128)                   # Text color in gray

def chapterTitle(self, fz, num, label):
    self.set_font('Arial', '',fz.size + 2 )                  # Arial 12
    self.set_fill_color(200, 220, 255)                       # Background color
    txt = num + " : " + label
    self.cell(0, 8, txt, 0, 1, 'L', 1, '')
    self.ln(4)                                               # Line break
    self.set_font(fz.family, fz.style, fz.size )
    self.set_text_color(128)                   # Text color in gray
    fz.ln = fz.ln + (fz.v_ln * 4) ; fz.lc += 4 # line size control(s)

def printLine(self, fz, linetopr):
    cn = fz.ci                                 # character number, create Page
    for c2 in linetopr:
         if fz.cp == True:
             createPage(self, fz)
         self.text(cn , fz.ln ,  c2 )
         cn += fz.v_cn                         # char size control

    fz.ln += fz.v_ln; fz.lc += 1               # line size control(s)

    if fz.lc == fz.ml:
       # pdfFooter(self, fz)
       fz.lc, fz.ln, fz.cp  = 0, fz.downlines, True   # Page is full

def formatLine(self, linetopr):
    self.addLine = 0
    if linetopr[0:1+1] == '#I':
        linetopr=linetopr.replace('#I','  ',1)
    if linetopr[0:3+1] == '#KEY':
        linetopr=linetopr.replace('#KEY','    ',1)

    if linetopr[0:6+1] == '# <EOR>':
        linetopr = ''  #-- 0123456

    if linetopr[0:8+1] == '#FILEUSED':
        linetopr = ''  #-- 012345678

    if linetopr[0:11+1] == '#FILE --#KEY':
        linetopr = ''   #-- 012345678901

    if linetopr[0:13+1] == '#FILE PERFORM=':
        linetopr, self.addLine = '',1
    if linetopr[0:13+1] == '#FILE USED...=':
        linetopr = ''
    if linetopr[0:13+1] == '#FILEUSED....=':
        linetopr = ''
    if linetopr[0:13+1] == '#FILE+PASSWRD=':
        linetopr = ''     # 01234567890123

    if linetopr[0:0+1] == '#':
        linetopr=linetopr.replace('#',' ',1)

    if linetopr[len(linetopr)-4:] == '#I|\n':
        linetopr = linetopr[0:len(linetopr)-4] + '\n'
    if linetopr[len(linetopr)-2:] == '|\n':
        linetopr = linetopr[0:len(linetopr)-2] + '\n'

    if linetopr[0:13+1] == ' FILE NAME   =':
        self.addLine = 1  # 01234567890123
        self.filehd  = linetopr[0:24]

    return linetopr
