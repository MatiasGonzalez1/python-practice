import moviepy

import moviepy.editor

#Ingresa la localizacion del archivo

video = moviepy.editor.VideoFileClip('')

audio = video.audio

audio.write_audiofile('new_audio.mp3')