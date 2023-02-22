import sys
import ffmpy

file = sys.argv[1]
filename, ext = file.split('.')

ff = ffmpy.FFmpeg(
 inputs={file: None},
 outputs={f'{filename}.mp3': ['-ab', '320k']}
)
ff.run()
