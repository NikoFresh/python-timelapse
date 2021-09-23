# Python timelapse

A simple CLI to create a timelapse given the images.
The only requirement is FFmpeg installed on the system.

```
usage: main.py [-h] [-s] [-c] [-d DURATION] [-r RESOLUTION] path

Create a timelapse from a folder of images

positional arguments:
  path                  Path to the folder with the images

optional arguments:
  -h, --help            show this help message and exit
  -s, --sort            Sort the files inside the folder
  -c, --clean_dir       Delete the files inside the img folder once the timelapse has been created
  -d DURATION, --duration DURATION
                        Set the video duration, in seconds. Default 30.
  -r RESOLUTION, --resolution RESOLUTION
                        Set the video resolution. Default 1440x1080.
```

[LICENSE](LICENSE)
