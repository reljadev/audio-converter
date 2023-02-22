# Audio converter

## Usage of converter script

Place the script into a directory containing your audio/video files. To convert the file to .mp3 file, 320kbps bitrate, run the following:
```
python3 converter.py filename.ext
```
where filename.ext is the full name of the audio file you are converting. Note that file has to have an extension, otherwise the script won't work.

## Usage of bot script

Place the script into a directory containing your audio/video files. Run the following command to test the website:
```
python3 bot.py filename
```
After script finishes, the converted file will be downloaded in the same directory with the name `filename.converted`.
