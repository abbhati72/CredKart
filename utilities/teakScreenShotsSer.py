from datetime import datetime
from pathlib import Path

from selenium import webdriver

base_dir = Path(__file__).resolve().parent.parent
screen_file_path = base_dir / "ScreenShots"


class Take_Screen_Shots():

    @staticmethod
    def getScreenShots(filename, driver):
        driver = webdriver.Chrome()

        now = datetime.now()
        formatted_date = now.strftime("%d_%m_%y_%H_%M_%S")
        print(formatted_date)
        print()
        driver.save_screenshot(f"{screen_file_path}/{filename}_{formatted_date}.png")


