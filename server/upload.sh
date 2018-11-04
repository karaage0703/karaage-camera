#!/bin/bash

ftp -n karaagecam.local << _EOD
user pi raspberry
passive
binary
cd karaage-camera
put pix2pix-outputs.png
#put $1
bye
_EOD
