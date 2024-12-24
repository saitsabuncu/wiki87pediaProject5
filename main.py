from tkinter import *
from wikipedia import *

FONT = ('Arial', 20)
window = Tk()
window.title('Wikipedia API')

def clear():
    myEntry.delete(0, END)
    myText.delete(1.0, END)

def search():
    try:
        set_lang('tr')
        result = summary(myEntry.get(), sentences=5)  # Özet çekiyoruz
        clear()
        myText.insert(1.0, result)
    except Exception as e:
        clear()
        myText.insert(1.0, f"Hata: {str(e)}")

myLabelFrame = LabelFrame(window, text='Search Wikipedia')
myLabelFrame.pack(padx=20, pady=20)
myEntry = Entry(myLabelFrame)
myEntry.pack(padx=20, pady=20, fill=X)

textFrame = Frame(window)
textFrame.pack(padx=20, fill=X)

verticalScroll = Scrollbar(textFrame, orient='vertical')
verticalScroll.pack(side=RIGHT, fill=Y)
horizontalScroll = Scrollbar(textFrame, orient='horizontal')
horizontalScroll.pack(side=BOTTOM, fill=X)

myText = Text(textFrame, yscrollcommand=verticalScroll.set, xscrollcommand=horizontalScroll.set, wrap='none')
myText.pack(fill=X)

verticalScroll.config(command=myText.yview)
horizontalScroll.config(command=myText.xview)

buttonFrame = Frame(window)
buttonFrame.pack(pady=10)

searchButton = Button(buttonFrame, text='Search', font=FONT, padx=10, pady=3, command=search)
searchButton.grid(row=0, column=0, padx=20)

clearButton = Button(buttonFrame, text='Clear', font=FONT, padx=10, pady=3, command=clear)
clearButton.grid(row=0, column=1, padx=20)

window.mainloop()
