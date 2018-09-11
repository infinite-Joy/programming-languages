import PyPDF2
pdf1File = open('Automate_the_Boring_Stuff_sample_ch17.pdf', 'rb')
pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
for pageNum in range(pdf1Reader.numPages):
     pageObj = pdf1Reader.getPage(pageNum)
     __import__('pdb').set_trace()
     pass
