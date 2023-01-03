from fpdf import FPDF
pdf = FPDF
images_list = ['./1.png', './2.png']

for i in images_list:
  pdf.add_page()
  pdf.image()

pdf.output('yourfile.pdf', "F")

##################NO TERMINADO###################