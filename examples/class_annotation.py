# -*- coding: utf-8 -*-
from annotator import Annotator
# Define the labels
labels = [{'name': 'porn', 'color': (1, 0, 0)},
        {'name': 'sluty', 'color': (0, 0, 1)},
        {'name': 'sexy', 'color': (0, 1, 1)},
        {'name': 'normal', 'color': (0, 1, 0)}]
# Initialise MuViLab

name='H.mp4'
fn='E:\\download\\593310496_saturdays85\\test\\%s'%name

clips_folder = './%s'%name.rsplit('.',1)[0]
# Split the main video into clips
annotator = Annotator(labels, clips_folder, annotation_file='%s.json'%name, N_show_approx=10)
import os
if not os.path.exists(clips_folder):
    os.mkdir(clips_folder)
    annotator.video_to_clips(fn, clips_folder, clip_length=1200, overlap=0, resize=0.5)
# Run the GUI
annotator.main()
