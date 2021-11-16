#!/usr/bin/env python
# coding: utf-8

# In[2]:


from tkinter import *
from moviepy.editor import *


# In[3]:


vid1 =  VideoFileClip("vid1.mp4")
vid2 =  VideoFileClip("vid2.mp4")
vid3 =  VideoFileClip("vid3.mp4")


# In[ ]:





# In[4]:


def mix():
    final_clip = concatenate_videoclips([vid1, vid2, vid3])
    final_clip.write_videofile("Final_video .mp4")


# In[ ]:





# In[5]:


def rotate():
    clip_rotate = vid1.fx(vfx.mirror_x)
    clip_rotate.write_videofile("Final_video.mp4")


# In[ ]:





# In[6]:


def resize():
    r=float(input("Enter video size: "))
    clip_resize = vid1.resize(r)
    clip_resize.write_videofile("Final_video.mp4")


# In[ ]:





# In[7]:


def Effects_speed():
    speed = float(input("Enter your speed: "))
    clip_speed = vid1.fx(vfx.speedx, speed)
    clip_speed.write_videofile("Final_video.mp4")


# In[ ]:





# In[8]:


def Effects_color():
    colour = float(input("Value of Darkness: "))
    clip_color = vid1.fx(vfx.colorx, colour)
    clip_color.write_videofile("Final_video.mp4")
    


# In[ ]:





# In[9]:


def trim():
    starting = int(input("Enter starting point here: "))
    ending = int(input("Enter ending point here: "))
    clip_trim = vid1.cutout(starting, ending)
    clip_trim.write_videofile("Final_video.mp4")


# In[ ]:





# In[10]:


from moviepy.editor import * 
def audio_file():
    #from moviepy.editor import*
    videoclip = VideoFileClip("vid1.mp4")
    audioclip = AudioFileClip("audio.mp3")
    new_audioclip = CompositeAudioClip([audioclip])
    videoclip.audio = new_audioclip
    videoclip.write_videofile("Final_video.mp4")


# In[ ]:





# In[13]:


import moviepy.editor as mp
import cv2

def texttovideo():
    cap = cv2.VideoCapture("vid4.mp4")
    while(True):
        ret, frame = cap.read()
        
        font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        
        cv2.putText(frame, 'Manike mage hite', (50, 50), font, 1, (0, 255, 255), 2, cv2.LINE_4)
        cv2.imshow('video', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    
    cap.release()
    
    cv2.destroyAllWindows()


# In[ ]:





# In[ ]:





# In[15]:


root = Tk()
root.title("Video Editor App")
root.geometry("900x450")
root.minsize(900,450)
root.maxsize(900,450)
root.config(bg="#232323")



label = Label(root, text = "Edit the Video", bg = "#232323", fg = "white",pady=5, font=('arial',20,'bold'))  
label.pack() 

#add text to video
b=Button(root, text="Add text to Video", relief=GROOVE, bg="#232323", fg="white", command=texttovideo)
b.pack(side="left", padx=20)
b.config(width=16, height=3)

#mix

b=Button(root, text="Mix", relief=GROOVE, bg="#232323", fg="white", command=mix)
b.pack(side="left", padx=20)
b.config(width=8, height=3)

#mirror

b=Button(root, text="Mirror", relief=GROOVE, bg="#232323", fg="white", command=rotate)
b.pack(side="left", padx=20)
b.config(width=8, height=3)

#resize

b=Button(root, text="Resize", relief=GROOVE, bg="#232323", fg="white", command=resize)
b.pack(side="left", padx=20)
b.config(width=8, height=3)

#speed

b=Button(root, text="Speed", relief=GROOVE, bg="#232323", fg="white", command=Effects_speed)
b.pack(side="left", padx=20)
b.config(width=8, height=3)

#colour

b=Button(root, text="Colour", relief=GROOVE, bg="#232323", fg="white", command=Effects_color)
b.pack(side="left", padx=20)
b.config(width=8, height=3)

#trim

b=Button(root, text="Trim", relief=GROOVE, bg="#232323", fg="white", command=trim)
b.pack(side="left", padx=20)
b.config(width=8, height=3)

#audio

b=Button(root, text="Audio", relief=GROOVE, bg="#232323", fg="white", command=audio_file)
b.pack(side="left", padx=20)
b.config(width=8, height=3)



root.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:




