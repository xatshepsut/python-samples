#!/bin/bash
DATE=$(date +"%Y-%m-%d_%H:%M:%S")
mkdir images
#fswebcam images/dump.jpg
fswebcam -r 1280x720 images/img_$DATE.jpg