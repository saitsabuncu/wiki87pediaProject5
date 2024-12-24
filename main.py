from tkinter import *
from wikipedia import *

# Global font ayarı
FONT = ('Arial', 20)

# Ana pencere oluşturma
window = Tk()
window.title('Wikipedia API')

def clear():
    """
    Giriş alanını ve metin kutusunu temizler.
    Kullanıcıdan alınan giriş ve sonuç metni sıfırlanır.
    """
    myEntry.delete(0, END)  # Giriş alanını temizle
    myText.delete(1.0, END)  # Metin kutusunu temizle

def search():
    """
    Kullanıcının girişine göre Wikipedia'dan özet bilgi çeker.
    - 'tr' dil ayarı kullanılarak Wikipedia'dan veri alınır.
    - Özet bilgisi alınır ve metin kutusuna eklenir.
    - Eğer bir hata oluşursa, hata mesajı metin kutusunda gösterilir.
    """
    try:
        set_lang('tr')  # Wikipedia dilini Türkçe olarak ayarla
        result = summary(myEntry.get(), sentences=5)  # Kullanıcı girişiyle Wikipedia özeti al
        clear()  # Temizle
        myText.insert(1.0, result)  # Sonucu metin kutusuna ekle
    except Exception as e:
        clear()
        myText.insert(1.0, f"Hata: {str(e)}")  # Hata mesajını metin kutusuna yazdır

# Giriş alanı için çerçeve
myLabelFrame = LabelFrame(window, text='Search Wikipedia')
myLabelFrame.pack(padx=20, pady=20)

# Kullanıcı giriş alanı
myEntry = Entry(myLabelFrame)
myEntry.pack(padx=20, pady=20, fill=X)

# Metin kutusu için çerçeve
textFrame = Frame(window)
textFrame.pack(padx=20, fill=X)

# Metin kutusu kaydırma çubukları
verticalScroll = Scrollbar(textFrame, orient='vertical')
verticalScroll.pack(side=RIGHT, fill=Y)

horizontalScroll = Scrollbar(textFrame, orient='horizontal')
horizontalScroll.pack(side=BOTTOM, fill=X)

# Metin kutusu
myText = Text(textFrame, yscrollcommand=verticalScroll.set, xscrollcommand=horizontalScroll.set, wrap='none')
myText.pack(fill=X)

# Kaydırma çubuklarını metin kutusuna bağla
verticalScroll.config(command=myText.yview)
horizontalScroll.config(command=myText.xview)

# Düğmeler için çerçeve
buttonFrame = Frame(window)
buttonFrame.pack(pady=10)

# Search düğmesi
searchButton = Button(buttonFrame, text='Search', font=FONT, padx=10, pady=3, command=search)
searchButton.grid(row=0, column=0, padx=20)

# Clear düğmesi
clearButton = Button(buttonFrame, text='Clear', font=FONT, padx=10, pady=3, command=clear)
clearButton.grid(row=0, column=1, padx=20)

# Ana döngü
window.mainloop()