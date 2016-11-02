from lettuce import world
from lettuce.django import django_url
from acceptance_tests.features.definitions.core import finder


def follow_link(text):
    link = finder.find_link_by_text(text)
    link.click()


def go_to_url(url):
    world.browser.get(django_url(url))
