from tkinter import *
from random import randint

root = Tk()
root.title('Picnic List')
root.geometry('400x400')
root.configure(background = 'snow')

items = ('apples', 'chocolate', 'raspberries', 'cookies', 'muffins', 'chips')

lblItems = Label(root, text = 'Items: ' + str(items), bg = 'light blue')
lblItems.place(relx = 0.5, rely = 0.4, anchor = CENTER)

lblPutItem = Label(root, text = '', bg = 'light blue')
lblPutItem.place(relx = 0.5, rely = 0.6, anchor = CENTER)

def putItem():
    itemStr = str(randint(1, len(items)))
    if len(itemStr) >= 2:
        if itemStr[-2] == '1':
            itemStr += 'th'
    elif itemStr[-1] == '1':
        itemStr += 'st'
    elif itemStr[-1] == '2':
        itemStr += 'nd'
    elif itemStr[-1] == '3':
        itemStr += 'rd'
    else:
        itemStr += 'th'
    lblPutItem['text'] = f'Put the { itemStr } item in the bag!'

btnPutItem = Button(root, text = 'What item should I put?', command = lambda: putItem())
btnPutItem.place(relx = 0.5, rely = 0.5, anchor = CENTER)

root.mainloop()