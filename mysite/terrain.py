import datetime
import os
from django.core.management import call_command
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from lettuce import before, after, world
from django.conf import settings
import shutil


class SeleniumCache(object):
    data = {}

    def __init__(self):
        self.data = {}

    def set(self, key, val):
        self.data[key] = val

    def get(self, key):
        return self.data[key]

    def delete(self, key):
        del self.data[key]


@before.runserver
def create_db(args):
    call_command('restore_db', interactive=False, verbosity=0)
    db_name = settings.DATABASES['default']['NAME']
    shutil.copyfile(db_name, db_name + 'cp')


@before.all
def initial_setup():
    world.browser = webdriver.Firefox()
    world.browser.implicitly_wait(5)
    world.browser.set_window_size(1500, 1500)
    world.cache = SeleniumCache()
    world.to_find_overlay_xpath = ''
    world.wait = WebDriverWait(world.browser, 20)


@after.all
def teardown_browser(total):
    world.browser.quit()


@after.each_scenario
def screenshot_on_error(scenario):
    """
    Save a screenshot to help with debugging.
    """
    if scenario.failed:
        file_path = '/tmp/jenkins/last_failed_scenario_%s.png' % (datetime.datetime.now())
        if not os.path.isdir('/tmp/jenkins'):
            os.mkdir('/tmp/jenkins')
        world.browser.save_screenshot(file_path)
    world.browser.delete_all_cookies()


@before.each_scenario
def update_db(scenario):
    db_name = settings.DATABASES['default']['NAME']
    db_copy = db_name + 'cp'
    shutil.copyfile(db_copy, db_name)
