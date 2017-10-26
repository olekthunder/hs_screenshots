"""
    Module provides function to move Hearthstone Screenshots
    from Desktop to one directory
"""
import os
import sys
import logging
import re

# Directory's to move screenshots name
DIR_NAME = "Hearthstone Screenshots"

# Logging setup
logging.basicConfig(filename="hs_screnshots.log", level=logging.DEBUG,
                    format='(%(asctime)s) [%(levelname)s]: %(message)s',
                    datefmt='%d.%m.%Y %I:%M:%S')
LOGGER = logging.getLogger("hs_screenshots")

# Checking if Windows system variable is set
if "HOMEPATH" in os.environ:
    DESKTOP_PATH = os.path.join(os.environ.get("HOMEPATH"), "Desktop")
    SCREENSHOT_DIRECTORY = os.path.join(DESKTOP_PATH, DIR_NAME)
else:
    ERROR_MESSAGE = "Enviromental variable HOMEPATH is not set"
    LOGGER.critical(ERROR_MESSAGE)
    sys.exit(ERROR_MESSAGE)


def move_hs_screenshots():
    """
       Moves HSScreenshots to custom directory
    """
    # Moved files counter. Mostly for logging purposes
    count = 0
    pattern = re.compile(r"Hearthstone\sScreenshot.*\.png")
    # Moving files
    for file in os.listdir(DESKTOP_PATH):
        if pattern.match(file):
            full_file_path = os.path.join(DESKTOP_PATH, file)
            new_file_path = os.path.join(SCREENSHOT_DIRECTORY, file)
            os.renames(full_file_path, new_file_path)
            count += 1
    if count != 0:
        LOGGER.info("Moved {0:d} files to {1:s}".format(count,
                                                        SCREENSHOT_DIRECTORY))

if __name__ == "__main__":
    move_hs_screenshots()
