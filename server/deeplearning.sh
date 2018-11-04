#!/bin/bash

cp $1 ~/GitHub/pix2pix-tensorflow/test.jpg
cd ~/GitHub/pix2pix-tensorflow
python pix2pix_test.py --mode test --output_dir pix2pix_test --checkpoint pix2pix_train --input_img test.jpg
mv pix2pix-outputs.png ~/GitHub/karaage-camera/server/
