# pygiffer
>  A python script to make gifs from videos using Python and ffmpg

This script was originally a bash script but was rewritten in python
for the sake of learning how to write scripts using Python.

# Requirements

The only requirement at the moment is to have ffmpeg installed and for
it to be usable from the command line.

# Usage

To create a gif using this script simply call the program either by
itself or using the python interpreter and dive it the 4 required
arguments: an input video source, a time stamp either in seconds from
the beginning or formated as HH:MM:SS where the start of the video
is, a duration in seconds of approximately where the gif ends and
the name of the gif with it's extension.

~~~
$ python pygiffer.py input.avi start_time duration output.gif
~~~

~~~
$ ./pygiffer.py input.avi start_time duration output.gif
~~~

This will first make a new folder called `output` containing the frames
extracted from the video source from the time stamp given to the end of
the duration.

This folder is created so that you can fine tune the beginning and end
of the gif for better looping.

You will be asked to select the starting and ending frames, that match
with the file names of the extracted frames.

Now the gif will be created using ffmpeg and the directory containing
the frames will be deleted.

# Flags

There are four flags that are used to control the characteristics of
the output gif:

* `-w` or `--width` to define the width of the output gif, by default 540.
* `-f` or `--fps` to define the frames per second of the output gif, by default 15.
* `--ffps` to match the fps of the output with the input.
* `-c` or `--crop` to create a gif from cropped frames. The option has
has to be formated: W:H:X:Y


