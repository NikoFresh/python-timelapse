import argparse
import os
import sys

from timelapse import Timelapse
from utils import clean_dir, reorder_files

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
    "-c",
    "--clean_dir",
    action="store_true",
    help="Delete the files inside the img folder once the timelapse has been created",
)

parser.add_argument(
    "-d",
    "--duration",
    action="store",
    help="Set the video duration, in seconds. Default 30.",
    type=int,
)

parser.add_argument(
    "-r",
    "--resolution",
    action="store",
    help="Set the video resolution. Default 1440x1080.",
    type=str,
)


if __name__ == "__main__":
    args = parser.parse_args()

    if not os.path.isdir(args.Path):
        print("The path specified does not exist")
        sys.exit()

    if not any(os.scandir(args.Path)):
        print("The path specified is empty")
        sys.exit()

    timelapse = Timelapse(args.Path)

    if args.sort:
        print("Sorting the files...", end=" ", flush=True)
        reorder_files(args.Path)
        print("Done")

    if args.duration:
        print(
            f"Setting the duration to {args.duration} seconds...", end=" ", flush=True
        )
        timelapse.set_duration(args.duration)
        print("Done")

    if args.resolution:
        print(f"Setting the resolution to {args.resolution}...", end=" ", flush=True)
        timelapse.set_resolution(args.resolution)
        print("Done")

    current_settings = timelapse.get_settings()
    print("Current settings:")
    for key, value in current_settings.items():
        formatted_key = "- " + key.capitalize() + ":"
        print(f"{formatted_key: <20} {value: <20}")

    print("Creating the timelapse...", end=" ", flush=True)
    timelapse.create_video()
    print("Done")

    if args.clean_dir:
        print("Cleaning up the folder...", end=" ", flush=True)
        clean_dir(args.Path)
        print("Done")

    sys.exit()
