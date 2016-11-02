"""
This module implements common functions for interacting with forms.
"""
from lettuce import world

from acceptance_tests.features.definitions.core import finder


def enter_into_field(field_name, text):
    """
    Enters text into field.

    Args:
        field_name (string): Name of field to enter to.
        text (string): Text to enter.
    """
    input_el = finder.find_element_by_name(field_name)
    _clear_and_send_keys_to_element(input_el, text)


def enter_into_ckeditor(text):
    source_activator = finder.find_element_by_class(
        'cke_button__source_label'
    )
    source_activator.click()
    textarea = finder.find_element_by_class('cke_source')
    _clear_and_send_keys_to_element(textarea, text)


def _clear_and_send_keys_to_element(el, text):
    remove_keys = u'\b' * 1000
    el.send_keys(remove_keys)
    el.send_keys(text)


def submit_form():
    """
    Submits the first form in the page.
    """
    form = finder.find_form()
    form.submit()


def submit_form_with_id(id):
    """
    Submits form with id
    """
    form = finder.find_element_by_id(id)
    form.submit()


def select_option(field_name, option_text):
    """
    Selects option in dropdown.

    Args:
        field_name (string): Name of dropdown to select in.
        option_text (string): Visible text in option to select.

    """
    select_el = finder.find_select_by_name(field_name)
    select_el.select_by_visible_text(option_text)


def click_button(text):
    """
    Clicks button with provided text.
    """
    link = finder.find_clickable_button_by_text(text)
    link.click()


def click_checkbox_by_label_text(field_name, text_in_label):
    """
    Clicks first checkbox that contain ``text_in_label`` in label text.

    Args:
        field_name (string): Name of checkbox to click.
        text_in_label (string): Text contained in label.
    """
    xpath = '//input[@name="%s"]/parent::label[contains(., "%s")]' % (
        field_name,
        text_in_label)
    el = finder.find_element_by_xpath(xpath)
    el.click()


def confirm_dialog_box():
    """
    Click ok or yes in browser's alert box
    """
    alert = world.browser.switch_to.alert
    alert.accept()


def uncheck_checkbox(element_id):
    checkbox = finder.find_element_by_id(element_id)
    if checkbox.get_attribute('checked') is not None:
        checkbox.click()


def check_checkbox(element_id):
    checkbox = finder.find_element_by_id(element_id)
    if checkbox.get_attribute('checked') is None:
        checkbox.click()


def select_radio_option_by_value(field_name, value):
    xpath = '//input[@type="radio" and @name="%s" and @value="%s"]' % (field_name,
                                                                       value)
    radio = finder.find_element_by_xpath(xpath)
    radio.click()
