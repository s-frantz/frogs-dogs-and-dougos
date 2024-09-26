import sys
import os
import time
import random
import traceback
import yaml
import pyperclip
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

sys.dont_write_bytecode = True
from froggos.get_activities_from_html import get_activities_from_html
from froggos.get_athlete_from_html import get_athlete_from_html
from froggos.get_weekday_from_html import get_weekday_from_html
from froggos.get_milesplits_from_html import get_milesplits_from_html
from froggos.get_comment_from_milesplits import get_comment_from_milesplits


# settings
PROD = False # switch to true to have code post comments

# urls
LOGIN_URL = "https://www.strava.com/login"
ATHLETES_URL = "https://www.strava.com/athletes"
ACTIVITIES_URL = "https://www.strava.com/activities"

# xpaths
USER_INPUT_XPATH = "/html/body/div[2]/div[2]/div/form/fieldset/div[1]/input"
PASS_INPUT_XPATH = "/html/body/div[2]/div[2]/div/form/fieldset/div[2]/input"
LOGIN_BUTTON_XPATH = "/html/body/div[2]/div[2]/div/form/button"
ACTIVITY_LOG_XPATH = "/html/body/div[1]/div[3]/div/div[3]/div[1]/div[2]/div[4]"

# globals
EASY_RUN_DAYS = ["monday", "tuesday", "thursday", "friday"]

# local files
ATHLETES_YAML = "athletes.yaml"
SCRATCH_DIR = "scratch"

# get .env vars
load_dotenv(override=True)
STRAVA_USER = os.getenv("STRAVA_USER")
STRAVA_PASS = os.getenv("STRAVA_PASS")

# launch driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def random_sleep(min=0.5, max=3.0):
    sleep_time = random.uniform(min, max)
    time.sleep(sleep_time)

def shuffle_dict(d):
    items = list(d.items())
    random.shuffle(items)
    return dict(items)

def get_athletes():
    """Read local athletes.yaml and return {athlete_name: athlete_id}"""
    with open(ATHLETES_YAML, "r") as f:
        return yaml.safe_load(f)

def get_attempt_file():
    return os.path.join(
        SCRATCH_DIR,
        f"{athlete_name}_{time.strftime('%Y%m%d')}.attempt"
    )

def get_invalid_file():
    return os.path.join(
        SCRATCH_DIR,
        f"{athlete_name}_{activity_id}.invalid"
    )

def get_complete_file():
    return os.path.join(
        SCRATCH_DIR,
        f"{athlete_name}_{activity_id}.complete"
    )

def write_attempt_file(message: str):
    print(message)
    with open(attempt_file_path, "w") as f:
        f.write(message)    

def write_invalid_file(message: str):
    print(message)
    with open(invalid_file_path, "w") as f:
        f.write(message)

def write_complete_file(message: str):
    print(message)
    with open(complete_file_path, "w", encoding="utf-8") as f:
        f.write(message)

def get_element(xpath):
    return driver.find_element(By.XPATH, xpath)

def log_in_to_strava():
    random_sleep()
    driver.get(LOGIN_URL)
    random_sleep()
    user_input_element = get_element(USER_INPUT_XPATH)
    user_input_element.send_keys(STRAVA_USER)
    random_sleep()
    pass_input_element = get_element(PASS_INPUT_XPATH)
    pass_input_element.send_keys(STRAVA_PASS)
    random_sleep()
    login_button_element = get_element(LOGIN_BUTTON_XPATH)
    login_button_element.click()

def get_athlete_activities():

    # go to athlete page
    random_sleep()
    athlete_url = f"{ATHLETES_URL}/{athlete_id}"
    driver.get(athlete_url)

    # list activities on the page
    random_sleep()
    html = driver.page_source
    return get_activities_from_html(html)

def activity_workflow():

    # navigate to activity page
    random_sleep()
    activity_url = f"{ACTIVITIES_URL}/{activity_id}"
    driver.get(activity_url)

    # read athlete and weekday from activity page
    random_sleep()
    html = driver.page_source
    athlete = get_athlete_from_html(html)
    weekday = get_weekday_from_html(html)

    # assert weekday is an easy run day
    assert weekday.lower() in EASY_RUN_DAYS, f"weekday: {weekday.lower()}"

    # assert athlete is expected
    assert athlete == athlete_name, f"athlete: {athlete}"

    # read milesplits and convert to comment
    milesplits_xpath = "/html/body/div[1]/div[3]/div/section/div[1]/div[1]/div"
    milesplits_element = get_element(milesplits_xpath)
    milesplits_html = milesplits_element.get_attribute('innerHTML')
    milesplits = get_milesplits_from_html(milesplits_html)
    assert milesplits, "no milesplits"
    comment = get_comment_from_milesplits(milesplits)

    # copy comment to clipboard
    pyperclip.copy(comment)

    # click to open comment window
    random_sleep()
    comment_button_xpath = "/html/body/div[1]/div[3]/section/header/div/div[2]/span/div/div/button"
    comment_button_element = get_element(comment_button_xpath)
    comment_button_element.click()

    # paste clipboard contents
    random_sleep()
    comment_area_xpath = "/html/body/reach-portal/div[2]/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/div/textarea"
    comment_area_element = get_element(comment_area_xpath)
    comment_area_element.send_keys(Keys.CONTROL + 'v')

    # submit comment
    random_sleep()
    comment_submit_xpath = "/html/body/reach-portal/div[2]/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div[3]/button"
    comment_submit_element = get_element(comment_submit_xpath)
    if PROD: comment_submit_element.click()

    return comment


if __name__ == "__main__":

    # make sure scratch directory exists
    if not os.path.exists(SCRATCH_DIR):
        os.makedirs(SCRATCH_DIR)

    # get athletes from yaml
    athletes = get_athletes()

    # log in to strava
    log_in_to_strava()

    # iterate through athletes
    for athlete_name, athlete_id in shuffle_dict(athletes).items():

        # define an attempt file for this athlete for today
        attempt_file_path = get_attempt_file()
        if os.path.exists(attempt_file_path):
            print(f"`{attempt_file_path}` exists")
            continue

        # get activities for the athlete
        try:
            activities = get_athlete_activities()
        except Exception as e:
            write_attempt_file(str(e))
            continue

        # iterate through activities
        for activity_id in activities:

            # bail if activity has failed before
            invalid_file_path = get_invalid_file()
            if os.path.exists(invalid_file_path):
                print(f"`{invalid_file_path}` exists")
                continue

            # bail if activity has been commented on already
            complete_file_path = get_complete_file()
            if os.path.exists(complete_file_path):
                print(f"`{complete_file_path}` exists")
                continue

            # post a comment or bail if something unexpected
            try:
                comment = activity_workflow()
                write_complete_file(comment)
            except Exception as e:
                write_invalid_file(traceback.format_exc())
