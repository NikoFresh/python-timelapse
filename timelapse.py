import os


class Timelapse:
    """
    TODO:
    - calculate the frame rate based on the lenght
    -
    """

    def __init__(self, dir: str) -> None:
        self.dir: str = dir

    def create_video(self):
        os.system(
            f'ffmpeg -framerate 30 -pattern_type glob -i "{self.dir}/*.jpg" -s:v 1440x1080 -c:v libx264 -crf 17 -pix_fmt yuv420p timelapse.mp4'
        )
