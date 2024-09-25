import sys
import os
import time
import random
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

sys.dont_write_bytecode = True
from froggos.get_activities_from_html import get_activities_from_html


# urls
LOGIN_URL = "https://www.strava.com/login"
ATHLETES_URL = "https://www.strava.com/athletes"
ACTIVITIES_URL = "https://www.strava.com/activities"

# xpaths
USER_INPUT_XPATH = "/html/body/div[2]/div[2]/div/form/fieldset/div[1]/input"
PASS_INPUT_XPATH = "/html/body/div[2]/div[2]/div/form/fieldset/div[2]/input"
LOGIN_BUTTON_XPATH = "/html/body/div[2]/div[2]/div/form/button"
ACTIVITY_LOG_XPATH = "/html/body/div[1]/div[3]/div/div[3]/div[1]/div[2]/div[4]"

#local dirs
SCRATCH_DIR = "scratch"

# get .env vars
load_dotenv(override=True)
STRAVA_USER = os.getenv("STRAVA_USER")
STRAVA_PASS = os.getenv("STRAVA_PASS")
ATHLETE_ID = os.getenv("ATHLETE_ID")
ATHLETE_NAME = os.getenv("ATHLETE_NAME")


def random_sleep(min=0.5, max=3.0):
    sleep_time = random.uniform(min, max)
    time.sleep(sleep_time)

def click_button(xpath):
    driver.find_element(By.XPATH, xpath).click()

def fill_input(xpath, text):
    driver.find_element(By.XPATH, xpath).send_keys(text)

def launch_selenium_driver():
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def log_in_to_strava():
    driver.get(LOGIN_URL)
    random_sleep()
    fill_input(USER_INPUT_XPATH, STRAVA_USER)
    random_sleep()
    fill_input(PASS_INPUT_XPATH, STRAVA_PASS)
    random_sleep()
    click_button(LOGIN_BUTTON_XPATH)

def get_athlete_activities():
    random_sleep()
    athlete_page_url = f'{ATHLETES_URL}/{ATHLETE_ID}'
    driver.get(athlete_page_url)
    random_sleep()
    html = driver.page_source
    return get_activities_from_html(html)

def get_activity_info(activity):
    """
    Provided an activity ID, returns a dict of:
    {
        "athlete": "First Last",
        "weekday": "Monday",
        "miles": ["8:18", "7:15", "6:50", "6:45", "8:03"]
    }
    """
    # initialize dict
    info = {}

    # navigate to activity
    activity_page_url = f'{ACTIVITIES_URL}/{activity}'
    driver.get(activity_page_url)
    random_sleep()

    # get html
    html = driver.page_source

    with open(r"C:\GitHub\frogs-dogs-and-dougos\activity.html", 'w') as f:
        f.write(html)

    breakpoint()

def process_activities(activities):

    # make sure scratch dir exists
    if not os.path.exists(SCRATCH_DIR):
        raise OSError(f"need scratch dir:\n\n`{SCRATCH_DIR}`")

    for activity in activities:

        # define dot_paths and exit if any already exist
        dot_complete_path = os.path.join(SCRATCH_DIR, activity + '.complete')
        dot_error_path = os.path.join(SCRATCH_DIR, activity + '.error')
        dot_working_path = os.path.join(SCRATCH_DIR, activity + '.working')
        if (
            os.path.exists(dot_complete_path)
            or os.path.exists(dot_error_path)
            or os.path.exists(dot_working_path)
        ):
            print(f"{activity} already processed")
            continue
        
        # create dot working
        with open(dot_working_path, 'w') as f:
            f.write("")

        # get activity info dict
        ## activity_info = get_activity_info(activity)

        # determine who did the activity

        # if someone other than the expected athlete, write a dot error
        ##if activity_athlete != ATHLETE_NAME:
        ##    with open(dot_error_path, 'w') as f:
        ##        f.write("")

def filter_athlete_activities():
    """
    It appears not all activities in the activity log will be from the profile athlete.
    Any activities that are not from the athlete can immediately be considered "complete".
    """
    return


if __name__ == '__main__':

    if False:

        # start up selenium driver
        driver = launch_selenium_driver()

        # log in to strava
        log_in_to_strava()

        # list activities
        activities = get_athlete_activities()

        assert activities == [
            '12429464990',
            '12419842701',
            '12410435514',
            '12402849066',
            '12402848492',
        ], f"ribbit, test(s) failed"

        print(f"bork, test(s) passed!")

    else:
        driver = launch_selenium_driver()
        #log_in_to_strava()
        
        activities = [
            '12429464990',
            '12419842701',
            '12410435514',
            '12402849066',
            '12402848492',
        ]

        for activity in activities:
            get_activity_info(activity)
            break
