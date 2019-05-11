# karaage-camera
All image will change to KARAAGE!

# Dependency

- Python3
- TensorFlow==1.8.0
- Keras==2.1.6

# Setup
## Clone repository and Download weight parameter

```sh
$ cd && git clone https://github.com/karaage0703/karaage-camera
$ cd karaage-camera/model
$ wget https://www.dropbox.com/s/3vk171n8jroxqt7/karaage_gen_weight.hdf5?dl=0 -O karaage_gen_weight.hdf5
```

## Auto Boot

Execute following commands for auto boot of karaage-camera:

```sh
$ sudo cp ~/karaage-camera/service/karaage_cam.service /etc/systemd/system/
$ sudo systemctl daemon-reload
$ sudo systemctl enable karaage_cam.service
```

If you want to stop auto boot, execute following command:
```sh
$ sudo systemctl disable karaage_cam.service
```

# Usage


# License
This software is released under the MIT License, see LICENSE.

# Authors
karaage0703

# References
