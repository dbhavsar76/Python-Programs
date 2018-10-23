from tkinter import *
from tkinter import messagebox

def encode():
    ustring = entry1.get()
    estring = ''
    key = entry2.get()
    if key.isdigit() == 0:
        msg = messagebox.showerror('Unexpected Input','Shift Count must be an Integer.')
    else:    
        for ch in ustring:
            if ch.isalpha():
                x = ord(ch)
                if x > ord('Z'):
                    x -= 32
                x += int(key)
                if x > ord('Z'):
                    x -= 26
                elif x < ord('A'):
                    x += 26
                estring += chr(x)
            elif ch == " ":
                estring += " "
        text1.delete(1.0, 1.99)
        text1.insert(INSERT, estring)

def decode():
    ustring = entry1.get()
    estring = ''
    key = entry2.get()
    if key.isdigit() == 0:
        msg = messagebox.showerror('Unexpected Input','Shift Count must be an Integer.')
    else:
        for ch in ustring:
            if ch.isalpha():
                x = ord(ch)
                if x > ord('Z'):
                    x -= 32
                x -= int(key)
                if x > ord('Z'):
                    x -= 26
                elif x < ord('A'):
                    x += 26
                estring += chr(x)
            elif ch == " ":
                estring += " "
        text1.delete(1.0, 1.99)
        text1.insert(INSERT, estring)

root=Tk()
#root.geometry('400x600')
root.title('Caesar Cipher')
root.resizable(NO, NO)
#root.maxsize(400,600)

label1=Label(root, text='Caesar Encoder And Decoder', font='12')
label1.grid(padx='5', pady='15', row='0',columnspan='2')

label2=Label(root, text='Enter Text')
label2.grid(padx='5', pady='10', row='1', column='0', sticky=E)

entry1=Entry(root, justify=LEFT, width='50')
entry1.grid(padx='5', pady='10', row='1', column='1', sticky=W)

label3=Label(root, text='Shift Count')
label3.grid(padx='5', pady='10', row='2', column='0', sticky=E)

entry2=Entry(root, justify=LEFT, width='3')
entry2.grid(padx='5', pady='10', row='2', column='1', sticky=W)

encodeButton=Button(root, text='Encode', command=encode)
encodeButton.grid(padx='5', pady='10', row='3', column='0', ipadx='25', sticky=E)

decodeButton=Button(root, text='Decode', command=decode)
decodeButton.grid(padx='5', pady='10', row='3', column='1', ipadx='25', sticky=W)

label4=Label(root, text='Message')
label4.grid(padx='5', pady='10', row='4', column='0', sticky=E)

text1=Text(root, height='2', width='35')
text1.insert(INSERT, 'Encoded Message')
text1.grid(padx='5', pady='10', row='4', column='1', sticky=W)

root.mainloop()