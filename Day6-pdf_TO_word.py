
#PDF TO DOCX

from pdf2docx import Converter

old_pdf ="HUM111_Handouts_Lecture12.pdf" #change the name to your own .pdf file
new_doc ="new.docx"

obj = Converter(old_pdf)
obj.convert(new_doc)

obj.close

#DOCX TO PDF
'''

from docx2pdf import convert

convert("new.docx","new_pdf.pdf")

'''