import argparse
import os
import sys

from timelapse import Timelapse
from utils import reorder_files


parser = argparse.ArgumentParser(
    description="Create a timelapse from a folder of images"
)

# Add the arguments
parser.add_argument(
    "Path", metavar="path", type=str, help="Path to the folder with the images"
)

parser.add_argument(
    "-s", "--sort", action="store_true", help="Sort the files inside the folder"
)

parser.add_argument(
    "-d",
    "--duration",
    action="store",
    help="Set the video duration, in seconds",
    type=int,
)

parser.add_argument(
    "-r", "--resolution", action="store", help="Set the video resolution, in pixels."
)


if __name__ == "__main__":
    args = parser.parse_args()

    if not os.path.isdir(args.Path):
        print("The path specified does not exist")
        sys.exit()

    timelapse = Timelapse(args.Path)

    if args.sort:
        print("Sorting the files...", end=" ")
        reorder_files(args.Path)
        print("Done")

    if args.duration:
        print(f"Setting the duration to {args.duration} seconds...", end=" ")
        timelapse.set_duration(args.duration)
        print("Done")

    timelapse.create_video()
