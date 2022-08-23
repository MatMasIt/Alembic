from PyPDF3 import PdfFileWriter, PdfFileReader
from PyPDF3.pdf import PageObject


alembic = PdfFileReader(open("Alembic.pdf", "rb"), strict=False)

output = PdfFileWriter()
n = alembic.numPages
for i in range(n//2):
  if not i%2:
    print(n-i,i+1)
    page1 = alembic.getPage(n-i-1)
    page2 = alembic.getPage(i+1-1)
  else:
    print(i+1,n-i)
    page1 = alembic.getPage(i+1-1)
    page2 = alembic.getPage(n-i-1)

  total_width = page1.mediaBox.upperRight[0] + page2.mediaBox.upperRight[0]
  total_height = max([page1.mediaBox.upperRight[1], page2.mediaBox.upperRight[1]])
  
  new_page = PageObject.createBlankPage(None, total_width, total_height)

  # Add first page at the 0,0 position
  new_page.mergePage(page1)
  # Add second page with moving along the axis x
  new_page.mergeTranslatedPage(page2, page1.mediaBox.upperRight[0], 0)
  output.addPage(new_page)
output.write(open("paged.pdf", "wb"))

