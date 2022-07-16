import pyttsx3
import PyPDF2
book = open('The Seven Husbands of Evelyn Hugo (Taylor Jenkins Reid) (z-lib.org).pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
Speaker = pyttsx3.init()
for num in range(10, pages):
    page = pdfReader.getPage(7)
    text = page.extractText()
    Speaker.say(text)
    Speaker.runAndWait()
