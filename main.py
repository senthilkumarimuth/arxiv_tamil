from textblob import TextBlob
import PyPDF2



with open("the-lion-and-the-rabbit-pdf.pdf", "rb") as pdf_file:
    read_pdf = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in read_pdf.pages:
        text += page.extract_text() + "\n"
        print(text)

word=TextBlob(text)
Translate_text = word.translate(from_lang='en',to='ta')
print(Translate_text)