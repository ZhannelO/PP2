from tracemalloc import stop
import pygame 
import tkinter as tk
import os
import fnmatch
pygame.init()
pygame.mixer.music.load('music/tpn.ogg')
screen= tk.Tk()
screen.title("Zhantify")
screen.geometry("600x800")
screen.config(bg='green')
rootpath="D:\music"
pattern="*.ogg"
prev_img=tk.PhotoImage(file="buttoms/prev_img.png")
stop_img=tk.PhotoImage(file="buttoms/pause_img.png")
next_img=tk.PhotoImage(file="buttoms/buttnext.png")
play_img=tk.PhotoImage(file="buttoms/play_img.png")
def select():
    label.config(text=listBox.get("anchor"))
    pygame.mixer.music.load(rootpath +"\\"+listBox.get("anchor"))
    pygame.mixer.music.play()
def stop():
    pygame.mixer.music.stop()
    listBox.select_clear("active")

def play_next():
    next_song=listBox.curselection()
    next_song=next_song[0]+1
    next_song_name=listBox.get(next_song)
    label.config(text=next_song_name)
    pygame.mixer.music.load(rootpath +"\\"+next_song_name)
    pygame.mixer.music.play()

    listBox.select_clear(0,'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)
def prev_next():
    next_song=listBox.curselection()
    next_song=next_song[0]-1
    next_song_name=listBox.get(next_song)
    label.config(text=next_song_name)
    pygame.mixer.music.load(rootpath +"\\"+next_song_name)
    pygame.mixer.music.play()

    listBox.select_clear(0,'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)

listBox=tk.Listbox(screen,fg="black",bg="green",width=100,font=("poppins",18))
listBox.pack(padx=15,pady=15)
for root ,dirs,files in os.walk(rootpath):
    for filename in fnmatch.filter(files,pattern):
        listBox.insert('end',filename)

label=tk.Label(screen,text='',bg='green',fg='blue',font=("poppins",18))
label.pack(pady=15)
top=tk.Frame(screen,bg="green")
top.pack(padx=10,pady=5,anchor="center")
prev=tk.Button(screen,text="Prev",image=prev_img,bg="green",borderwidth=0,command=prev_next)
prev.pack(pady=15,in_=top,side='left')
stop_buttom=tk.Button(screen,text="Stop",image=stop_img,bg="green",borderwidth=0,command=stop)
stop_buttom.pack(pady=15,in_=top,side="left")
play=tk.Button(screen,text="Play",image=play_img,bg="green",borderwidth=0,command=select)
play.pack(pady=15,in_=top,side='left')
next=tk.Button(screen,text="Next",image=next_img,bg="green",borderwidth=0,command=play_next)
next.pack(pady=15,in_=top,side='left')




screen.mainloop()
clock=pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill((255,255,255))
    pygame.display.flip()
    clock.tick(60)