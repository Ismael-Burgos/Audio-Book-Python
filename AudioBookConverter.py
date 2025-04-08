# Importing required libraries 
import pyttsx3 #for text to speech conversion
import PyPDF2 #for reading pdf files
from tkinter.filedialog import * #opening a file dialog to select pdf

#Open a file dialog for the user to select a pdf file
book = askopenfilename()

#Create a pdf reader object using the file
pdfreader = PyPDF2.PdfReader(book)

#get the total number of pages in the pdf
pages = len(pdfreader.pages)

#Loop through each page of the pdf
for num in range(0, pages):
    #Access the page by index
    page = pdfreader.pages[num]
    #Extract text content from page
    text = page.extract_text()
    #Initialize text to speech engine
    player = pyttsx3.init()
    #use text to speech engine to say the text
    player.say(text)
    #Wait until speaking is finished before moving to next page
    player.runAndWait()