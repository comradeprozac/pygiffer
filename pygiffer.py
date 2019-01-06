#!/usr/bin/env python
import os
import argparse
import subprocess

parser = argparse.ArgumentParser(description="Make GIFs with ffmpeg")

parser.add_argument('input_file', help="Input file")
parser.add_argument('start_time', help="Time stamp from the begining of the video where the frames will be stracted (HH:MM:SS.mm)")
parser.add_argument('duration', help="Duration of frames to be extracted")
parser.add_argument('output_file', help="Name of the output gif")

parser.add_argument(
    '-w', '--width', dest='width', default=540,
    help='Specify the width of the output GIF')
parser.add_argument(
    '-f', '--fps', dest='fps', default=15,
    help='Specify the Frames Per Second of the output GIF')
parser.add_argument(
    '--ffps', action='store_true', dest='ffps', default=False,
    help='Set fps to source')
parser.add_argument('-c', '--crop', dest='crop', default="", help='Crop the video to the specified dimensions and coordinates. They have to be specified in this form: WIDTH:HEIGHT:X:Y')

args = parser.parse_args()

if args.ffps:
    fps = ""
else:
    fps = "fps={}".format(args.fps)

framedir = os.path.splitext(args.output_file)[0]

if not os.path.exists(framedir):
    os.makedirs(framedir)

ffmpgcmd = [
    "ffmpeg", # 0
    "-v", "warning", # 1,2
    "-ss", args.start_time, # 3,4
    "-t", args.duration, # 5,6
    "-i", args.input_file, # 7,8
    "-vf", "scale=540:-1", # 9,10
    "-y", # 11
    framedir+"/frames%04d.png"] # 12

subprocess.run(ffmpgcmd)

print("Frames extracted to:\n{}/{}".format(os.getcwd(),framedir))

start_frame = int(input("Start gif in frame "))-1

final_frame = int(input("End gif in frame "))-1

if not args.crop=="":
    scale=""
    crop="crop={}".format(args.crop)
else:
    scale="scale={}:-1:flags=lanczos".format(args.width)
    crop=""

filters = "trim=start_frame={}:end_frame={},{},{}{}".format(start_frame,final_frame,fps,scale,crop)
ffmpgcmd[10] = filters+",palettegen"
ffmpgcmd[12] = "/tmp/palette.png"

subprocess.run(ffmpgcmd)

ffmpgcmd.insert(9,ffmpgcmd[12])
ffmpgcmd.insert(9,"-i")
ffmpgcmd[11] = "-lavfi"
ffmpgcmd[12] = filters+" [x]; [x][1:v] paletteuse"
ffmpgcmd[14] = args.output_file

subprocess.run(ffmpgcmd)

subprocess.run(["rm","-rf",framedir])

