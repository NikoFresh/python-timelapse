import os


class Timelapse:
    """
    TODO:
    - calculate the frame rate based on the lenght
    -
    """

    def __init__(self, dir: str) -> None:
        self.dir: str = dir
        self.duration: int = 30  # Video duration in seconds
        self.resolution: str = "1440x1080"  # Video resolution

    def create_video(self):
        os.system(
            f'ffmpeg -nostats -loglevel 0 -y -framerate {self.frame_rate()} -pattern_type glob -i "{self.dir}/*.jpg" -s:v {self.resolution} -c:v libx264 -crf 17 -pix_fmt yuv420p timelapse.mp4'
        )

    def frame_rate(self) -> int:
        """
        Calculate the frame rate based on the length of the video
        """
        # Count how many images are in the folder
        files = next(os.walk(self.dir))[2]
        n_images = len(files)
        # Return the frame rate
        return int(n_images / self.duration)

    def set_duration(self, duration: int) -> None:
        """
        Change the duration of the video, in seconds.
        """
        self.duration = duration

    def set_resolution(self, resolution: str) -> None:
        """
        Change the resolution of the video. Default 1440x1080.
        """
        self.resolution = resolution
