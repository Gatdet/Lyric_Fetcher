import lyricsgenius
from tkinter import *
from tkinter import scrolledtext


screen = Tk()
screen.title("Lyric Fetcher")
screen.config(bg="#ffff64")
screen.state('zoomed')


artist_label = Label(screen,  font=("Arial", 12, "bold"), text="Enter artist name:")
song_label = Label(screen, font=("Arial", 12, "bold"), text="Enter song name:")
artist_entry = Entry(screen,font=("Arial", 12, "bold"))
song_entry = Entry(screen,font=("Arial", 12, "bold"))
lyrics = Label(screen, font=("Arial", 10), bg="#ffff64")
scrollbar =Scrollbar(screen, orient= "vertical")
frame = Frame(screen)
frame.place(relwidth=0.8, relheight=0.65, relx=0.1, rely=0.25)
text_area = scrolledtext.ScrolledText(frame, font= ("Arial", 12), wrap = WORD)
text_area.configure(state ='normal')
text_area.place(relwidth=1.0, relheight=1.0)



def lookup(dont_worry_about_this_para):
    try:
        
        global artist_entry,song_entry
        text_area.delete('1.0','end')
        artist = genius.search_artist(artist_entry.get(), max_songs=0, sort="title")
        song = artist.song(song_entry.get())
        lyrics.config(text=song.lyrics)
        text_area.insert(INSERT, song.lyrics)
    
    except AttributeError:
        text_area.insert(INSERT, "DID YOU SPEEL CORRECTLY?")
     
        

button = Button(screen, text="Grab Lyrics",font=("Arial", 12, "bold"), command=lookup)
artist_label.place(x=40, y=40)
song_label.place(x=40, y=100)
artist_entry.place(x=180, y=40, width=500)
song_entry.place(x=180, y= 100, width=500)
button.place(x=10, y=180)
#lyrics.place(x=600, y=10)
scrollbar.pack(side= RIGHT, fill= BOTH)
logo_text = Label(screen, font=("Arial", 20, "bold"), text="L Y R I C    F E T C H E R", bg="#ffff64")
logo_text.place(x=900,y=30)
screen.bind("<Return>", lookup)
token = "5tleqhhI99YYNS2IDFbw3J246H_P_vyczkLA2lUjpfgf4sXQsZUxh3Yza0o4OfI1"
genius = lyricsgenius.Genius(token)

screen.mainloop()

