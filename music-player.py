#import libraries 
from pygame import mixer
from tkinter import *
import tkinter.font as font
from tkinter import filedialog


#add  ongs to the playlist
def addsongs():
    # list of songs is returned 
    temp_song=filedialog.askopenfilenames(initialdir="Music/",title="Choose a song", filetypes=(("mp3 Files","*.mp3"),))
    #loop through every song on the list
    for s in temp_song:
        s=s.replace("C:/Users/Boniface/Documents/Music/","")
        songs_list.insert(END,s)
        
            
def deletesong():
    curr_song=songs_list.curselection()
    songs_list.delete(curr_song[0])
    
    
def Play():
    song=songs_list.get(ACTIVE)
    song=f'C:/Users/Boniface/Documents/Music/{song}'
    mixer.music.load(song)
    mixer.music.play()

# pause the song 
def Pause():
    mixer.music.pause()

# stop the  song 
def Stop():
    mixer.music.stop()
    songs_list.selection_clear(ACTIVE)

# resume the song

def Resume():
    mixer.music.unpause()

#Function to navigate from the current song
def Previous():
    #to get the selected song index
    previous_one=songs_list.curselection()
    #to get the previous song index
    previous_one=previous_one[0]-1
    #to get the previous song
    temp2=songs_list.get(previous_one)
    temp2=f'C:/Users/Boniface/Documents/Music/{temp2}'
    mixer.music.load(temp2)
    mixer.music.play()
    songs_list.selection_clear(0,END)
    #activate new song
    songs_list.activate(previous_one)
    #set the next song
    songs_list.selection_set(previous_one)

def Next():
    # to get the selected song index
    next_one = songs_list.curselection()
    if not next_one:
        return

    # to get the next song index
    next_one = next_one[0] + 1
    if next_one >= songs_list.size():
        next_one = 0

    # to get the next song
    temp = songs_list.get(next_one)
    temp = f'C:/Users/Boniface/Documents/Music/{temp}'
    mixer.music.load(temp)
    mixer.music.play()

    songs_list.selection_clear(0, END)
    # activate new song
    songs_list.activate(next_one)
    # set the next song
    songs_list.selection_set(next_one)


# Creating the root window
root = Tk()
root.title(' Music player App ')
root.configure(bg='white')  # Set the background color to white

# Initialize mixer
mixer.init()

# Stylish font settings
listbox_font = font.Font(family='Segoe UI', size=15, weight='normal')
button_font = font.Font(family='Segoe UI', size=12, weight='bold')

# Create the listbox to contain songs with updated font settings
songs_list = Listbox(root, selectmode=SINGLE, bg="black", fg="white",
                     font=listbox_font, height=12, width=47, selectbackground="gray", selectforeground="black")
songs_list.grid(row=1, column=0, columnspan=6)  # Adjusted grid placement



# Buttons with updated font settings
play_button = Button(root, text="Play", width=7, command=Play, font=button_font, bg='black', fg='white')
pause_button = Button(root, text="Pause", width=7, command=Pause, font=button_font, bg='black', fg='white')
stop_button = Button(root, text="Stop", width=7, command=Stop, font=button_font, bg='black', fg='white')
Resume_button = Button(root, text="Resume", width=7, command=Resume, font=button_font, bg='black', fg='white')
previous_button = Button(root, text="Prev", width=7, command=Previous, font=button_font, bg='black', fg='white')
next_button = Button(root, text="Next", width=7, command=Next, font=button_font, bg='black', fg='white')



# Buttons placement within the grid
play_button.grid(row=2, column=0)
pause_button.grid(row=2, column=1)
stop_button.grid(row=2, column=2)
Resume_button.grid(row=2, column=3)
previous_button.grid(row=2, column=4)
next_button.grid(row=2, column=5)



# Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Submenu "Menu"
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Menu", menu=add_song_menu)
add_song_menu.add_command(label="Add songs", command=addsongs)
add_song_menu.add_command(label="Delete song", command=deletesong)

mainloop()


