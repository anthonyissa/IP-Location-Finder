import geocoder, os, socket
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('IP Location Finder')
root.wm_iconbitmap('ip.ico')
root.config(bg='#ff6d6d')
root.minsize(500, 300)
root.maxsize(500, 300)
root.grid()
Frame = Frame()

img = Image.open("ip.ico")
img = img.resize((100, 100))
img = ImageTk.PhotoImage(img)


Image = Label(root, bg='#ff6d6d', image=img)
Image.pack(pady=30)
Label(root, bg='#ff6d6d', text='ENTER THE IP', font=('Calibri bold',15)).place(rely=0.45, relx=0.382)

address = StringVar()
Entry(root, textvariable=address,width=30, justify='center',font=('Calibri bold',15)).place(rely=0.57, relx=0.19)

def getLocation():
    valid = True
    ip = address.get()
    try:
        socket.inet_aton(ip)
    except :
        valid = False
        Label(root, text='INVALID IP ADDRESS',bg='#ff6d6d' , fg='white',font=('Calibri bold',15)).place(rely=0.85, relx=0.323)

    if valid:
        g = geocoder.ip(ip)

        infos: str = str(g.geojson)
        infos = infos.replace("'", '').replace(',', '\n').replace('(', '').replace(')', '').replace('[', '').replace(']',
                                                                                                                         '') \
           .replace('{', '').replace('}', '')

        for line in infos.split('\n'):
            if "readme" in line:
               infos = infos.replace(line, '')

        try:
            os.mkdir('output')
        except:
            print('Ok')

        open(f'output/{ip}.txt', 'w').write(f'{infos}')
        root.destroy()


submit = Button(root, command=getLocation ,text='Submit', relief=GROOVE, bg='white', font=('Calibri',11)).pack(expand=YES)

root.mainloop()
