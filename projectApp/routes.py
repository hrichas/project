import PyPDF2
from PyPDF2 import PdfFileReader, PdfFileWriter
from projectApp import app
from flask import render_template



@app.route('/')
def index():
	pdf =[]
	pdfFileObj = PdfFileReader(open('/home/hricha/project/projectApp/static/pdfs/pdf1.pdf', 'rb'))
	for i in range(pdfFileObj.getNumPages()):
		p = pdfFileObj.getPage(i)
		outfile = PdfFileWriter()
		outfile.addPage(p)
		with open ('/home/hricha/project/projectApp/static/split_pdf/page-%02d.pdf' % i, 'wb') as f:
			outfile.write(f)
			pdf.append(outfile)
	return render_template('index.html', outfile=pdf)








