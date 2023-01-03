from PyPDF2 import PdfFileWriter, PdfFileReader
import getpass

pdfwriter = PdfFileWriter()

pdf = PdfFileReader("")

for page_num in range(pdf.numPages):
  pdfwriter.addPage(pdf.getPage(page_num))

passw = getpass.getpass(prompt='Enter the password: ')
pdfwriter.encrypt(passw)
with open('ho.pdf', 'wb') as f:
  pdfwriter.write(f)