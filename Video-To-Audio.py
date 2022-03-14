import moviepy.editor
from tkinter.filedialog import *

try:
    vid = askopenfilename()
    video = moviepy.editor.VideoFileClip(vid)

    aud = video.audio
    filename = "demo.mp3"
    aud.write_audiofile(filename)

    print(f"{filename} downloaded successfully....")
except KeyError:
    print("Please select a video file.")

except AttributeError:
    print("File type not supported.")

except OSError:
    print("Warning!! System Error.")

