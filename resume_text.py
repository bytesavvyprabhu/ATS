import PyPDF2 as pdf



def pdf_text(file, mode):
    pdf_reader = pdf.PdfReader(file)
    text = ""

        # Iterate through all pages
    for page_num in range(len(pdf_reader.pages)):
            # Extract text from each page
        page = pdf_reader.pages[page_num]
        text += page.extract_text()

    return text


print(pdf_text("JD.pdf",'rb'))