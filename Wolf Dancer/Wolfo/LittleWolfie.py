import tkinter as tk
from PIL import Image, ImageTk
from itertools import count
import winsound


def RBGAImage(path):
    return Image.open(path).convert("RGBA")

class ImageLabel(tk.Label):
   #A label that displays the gif.
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        self.loc = 0
        self.frames = []

        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(self.frames) == 1:
            self.config(image=self.frames[0])
        else:
            self.next_frame()

    def unload(self):
        self.config(image="")
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)

#Defining the visaul aspects.
root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.overrideredirect(1)
root.attributes('-transparentcolor',
                'red')
root.config(bg='red')
x_coordinate = (screen_width/1.5)
y_coordinate = (screen_height/2.12)
root.geometry("+%d+%d" %(x_coordinate,y_coordinate))
root.lift()
root.wm_attributes("-topmost", 1)
root.call('wm', 'attributes', '.', '-topmost', True)
lbl = ImageLabel(root)
lbl.config(bg='red')
lbl.pack()
lbl.load("Good_Stuff/Wolf_Caramell.gif")

winsound.PlaySound("Good_Stuff/nightclub.wav", winsound.SND_ASYNC +  winsound.SND_LOOP)

def stop_sound(event=None):
    #Stops playing the song.

    winsound.PlaySound(None, winsound.SND_PURGE)  # Purge the sound

def return_sound(event=None):
    #Resumes the music playback.

    winsound.PlaySound("Good_Stuff/nightclub.wav", winsound.SND_ASYNC +  winsound.SND_LOOP)

def kill(event=None):
    #Closes the application.
    root.destroy()  # Terminate the Tkinter main loop and close the window

#Keybinds for the functions
root.bind('<q>', stop_sound)
root.bind('<r>', return_sound)
root.bind('<Escape>', kill)


root.mainloop()

