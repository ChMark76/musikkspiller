# Importerer nødvendige biblioteker og moduler
import os
from tkinter import *
from tkinter import filedialog
from pygame import mixer

# Starter tkinter for å lage GUI-vinduet
root = Tk()
root.geometry("516x700+340+10")
root.title("Musikkspiller")
root.config(bg='#ffffff')
root.resizable(False, False)
mixer.init()

# Variabel for å spore pause-status
paused = False

# Funksjon for å legge til musikk fra valgt mappe
def addMusic():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)
        print(songs)
        for song in songs:
            if song.endswith(".mp3"):
                Playlist.insert(END, song)

# Funksjon for å spille musikk
def playMusic():
    global paused
    if paused:
        mixer.music.unpause()
        paused = False
    else:
        music_name = Playlist.get(ACTIVE)
        print(music_name[0:-4])
        mixer.music.load(Playlist.get(ACTIVE))
        mixer.music.play()

# Funksjon for å pause musikk
def pauseMusic():
    global paused
    if not paused:
        mixer.music.pause()
        paused = True
    else:
        mixer.music.unpause()
        paused = False

# Funksjon for å justere volumet
def setVolume(val):
    volume = float(val) / 100
    mixer.music.set_volume(volume)

# Legger til GUI-elementer
lower_frm = Frame(root, bg="#ffffff", width=516, height=200)
lower_frm.place(x=0, y=00)

# Animasjon GIF 
frmcount = 32
frms = [PhotoImage(file= os.path.join(os.path.dirname(__file__), 'animation.gif'), format='gif -index %i' % i) for i in range(frmcount)]
def update(ind):
    frame = frms[ind]
    ind += 1
    if ind == frmcount:
        ind = 0
    lbl.config(image=frame)
    root.after(40, update, ind)

lbl = Label(root)
lbl.place(x=0, y=0)
root.after(0, update, 0)


# Ramme for knapper
frm_music = Frame(root, bd=2, relief=RIDGE, width=516, height=120)
frm_music.place(x=0, y=580)

# Spill-knapp
btn_play = PhotoImage(file= os.path.join(os.path.dirname(__file__), 'play.png'))
btn_p = Button(root, image=btn_play, bg='#ffffff', height=50, width=50, command=playMusic)
btn_p.place(x=225, y=516)

# Stopp-knapp
btn_stop = PhotoImage(file= os.path.join(os.path.dirname(__file__), 'stop.png'))
btn_s = Button(root, image=btn_stop, bg='#ffffff', height=50, width=50, command=mixer.music.stop)
btn_s.place(x=140, y=516)

# Pause-knapp
btn_pause = PhotoImage(file= os.path.join(os.path.dirname(__file__), 'pause.png'))
btn_ps = Button(root, image=btn_pause, bg='#ffffff', height=50, width=50, command=pauseMusic)
btn_ps.place(x=310, y=516)

# Knapp for å velge musikkmappe
btn_browse = Button(root, text="Velg musikkmappe", font=('Arial,bold', 15), fg="Black", bg="#68da66", width=48, command=addMusic)
btn_browse.place(x=0, y=475)

# Volumkontroll
scale = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=setVolume, length=200, bg='#ffffff')
scale.set(50)  # Startvolum 50%
scale.place(x=310, y=0)

# Spilleliste
Scroll = Scrollbar(frm_music)
Playlist = Listbox(frm_music, width=100, font=('Arial,bold', 15), bg='#ffffff', fg='#00ff00', selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=Scroll.set)
Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT, fill=Y)
Playlist.pack(side=RIGHT, fill=BOTH)

# Kjører GUI-vinduet
root.mainloop()
