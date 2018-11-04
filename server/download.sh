#!/bin/bash

ftp -n karaagecam.local << _EOD
user pi raspberry
passive
binary
cd photo_data
get $1
bye
_EOD
