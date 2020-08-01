# pip install pypdf2
# pipenv install pypdf2
# Use PIPENV (CTRL+SHIFT+P)

import PyPDF2

# Provided the PDF is in the current WD and OPENING IT IN BINARY MODE "rb" as second argument
open("first.pdf", "rb")


with open("first.pdf", "rb") as file:
    reader = PyPDF2.PdfFileReader(file)  # File reader accepts a file stream
    print(reader.numPages)  # Prints no of pages
    # Takes page index no and index of the first page is 0
    page = reader.getPage(0)
    # Rotating by 90 degrees in clockwise and THIS DOES NOT MODIFY THE ORIGINAL PDF  AND ONLY ROTATING THE PAGE OBJECT IN THE MEMORY
    page.rotateClockwise(90)
    # NO ARGUMENT IS PASS IN THE WRITER OBJECT - DEALING WITH THE WRITER OBJECT IN THE MEMORY AND NOT THE ACTUAL PDF
    writer = PyPDF2.PdfFileWriter()
    # ADDS THE PAGE OBJECT AT THE END OF THE PDF IN THE MEMORY
    writer.addPage(page)
    # writer.insertPage(page, 1) # INSERTING PAGE AT SPECIFIC INDEX
    # writer.insertBlankPage()
    # WRITING CHANGES IN THE FILE and FOR THAT WE NEED ANOTHER FILE STREAM
    # WILL OPEN A NEW FILE IN THE WRITTEN BINARY MODE "wb"
    with open("rotated.pdf", "wb") as output:
        writer.write(output)  # Making changes in thee memory in a file


# COMBINING MULTIPLE PDFs INTO SINGLE PDF

merger = PyPDF2.PdfFileMerger()
# Files to be merged are stored as anarray of files
file_names = ["first.pdf", "rotated.pdf"]

for file_name in file_names:
    merger.append(file_name)  # HAPPENING IN THE MEMORY

merger.write("combined.pdf")  # WILL SAVE AS A FILE
