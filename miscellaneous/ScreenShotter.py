import pyautogui
import os
import shutil


class ScreenShotter:

    FILE_EXTENSION = 'png'

    # Creates the screenshot object and initializes the directory it uses
    def __init__(self, path, region):
        self.path = path
        self.region = region
        self._init_dir()

    # Deletes all directories in the pictures directory, initializing the pictures directory for use
    def _init_dir(self):
        for turn in os.listdir(self.path):
            shutil.rmtree(f'{self.path}/{turn}')

    def save_screenshot(self, player, turn_number):
        # Create a directory for this turn if it doesn't exist
        new_dir_path = f'{self.path}/{str(turn_number)}'
        try:
            os.mkdir(new_dir_path)
        except FileExistsError:
            pass

        # Take the screenshot and save it to our directory
        pyautogui.screenshot(f'{new_dir_path}/{player.lower()}.{ScreenShotter.FILE_EXTENSION}', region=self.region)


