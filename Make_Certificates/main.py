from PyPDF2 import PdfWriter, PdfReader
import io
import os
import pandas as pd
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A3, A4
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.colors import black

NAME_FONT = pdfmetrics.registerFont(TTFont('GreatVibes-Regular', 'GreatVibes-Regular.ttf'))
FILEPATH =r"Excel_file.xlsx"
os.makedirs('certificates')

def make_certificate(PER_NAME, index_name,ii):
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=A4)
    can.setFillColor(black)
    can.setFont('GreatVibes-Regular', 24)
    
    # Calculate the position to center the name
    name_width = can.stringWidth(PER_NAME, 'GreatVibes-Regular', 24)
    center_x = (A4[1] - name_width) / 2
    
    # Draw the name
    can.drawString(center_x, 290, PER_NAME)
    
    # Draw the index name
    can.setFont('GreatVibes-Regular', 8)
    NAME_FONT = pdfmetrics.registerFont(TTFont('GreatVibes-Regular', 'GreatVibes-Regular.ttf'))
    index_width = can.stringWidth(index_name, 'GreatVibes-Regular', 4)
    index_center_x = (A4[1] - index_width) / 2
    can.drawString(index_center_x, 15, index_name)
    
    can.save()

    # Move to the beginning of the StringIO buffer
    packet.seek(0)

    # Create a new PDF with Reportlab
    new_pdf = PdfReader(packet)

    # Read your existing PDF
    existing_pdf = PdfReader(open("test_certificate.pdf", "rb"))
    output = PdfWriter()

    # Add the "watermark" (which is the new pdf) on the existing page
    page = existing_pdf.pages[0]
    page.merge_page(new_pdf.pages[0])
    output.add_page(page)

    # Finally, write "output" to a real file
    output_stream = open(f"certificates/{PER_NAME}_certificate.pdf", "wb")
    output.write(output_stream)
    output_stream.close()
    print(ii)



df = pd.read_excel(FILEPATH)


names = [x for x in df['Name']]
print(names)
print(len(names))

# Python program to print 
# duplicates from a list 
# of strings
def Repeat(x):
	_size = len(x)
	repeated = []
	for i in range(_size):
		k = i + 1
		for j in range(k, _size):
			if x[i] == x[j] and x[i] not in repeated:
				repeated.append(x[i])
	return repeated


print (Repeat(names))


# Make certsssssssss
i = 0
for name in names:
    i = i+1
    PER_NAME = name
    make_certificate(PER_NAME,f'Certificate number : {100+i}',i)
    print(PER_NAME)

