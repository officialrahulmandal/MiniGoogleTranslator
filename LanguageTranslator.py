from tkinter import *

a = Tk()
a.title("GOOGLE MINI TRANSLATER")
con = 'hello'
lan = 'lol'




def convert():
    from textblob import TextBlob
    h = str(w.get("1.0", 'end-1c'))

    # h=w.get()

    en_blob = TextBlob(h)
    b = Tk()
    b.geometry('700x700+200+200')
    global con
    con = str(en_blob.translate(to='hi'))
    global lan
    lan = str(en_blob.detect_language())
    # print('conversion in english :-'+str(con))
    # print('input language type :'+str(lan))
    Label(b, text='conversion in english :-' + con).grid(row=0)
    Label(b, text='input language type :-' + lan).grid(row=1)




def abcd():
    quit()


a.geometry('700x700+200+200')

w = Text(a, height=10, width=80)
w.pack()

c = Button(a, text="convert to hindi", command=convert)
c.pack()
d = Button(a, text="QUIT", command=abcd)
d.pack()
a.mainloop()
















