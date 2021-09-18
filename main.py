import os

from config import Config
from timelapse import Timelapse


def reorder_files(path: str) -> bool:
    """
    Remove any subdirectories in the given path and reorder the files in the
    directory adding the name of the directory to the filename
    """
    for dir in os.listdir(path):
        dir_path = os.path.join(path, dir)
        if os.path.isdir(dir_path):
            for file in os.listdir(dir_path):
                file_path = os.path.join(dir_path, file)
                os.rename(file_path, os.path.join(path, dir + "_" + file))
            os.rmdir(dir_path)
    return True


def main() -> None:
    # TODO
    print("Reordering the images")
    reorder_files(Config.img_dir)
    print("Done")


if __name__ == "__main__":
    main()
