"""
This module contains functions that implement browser interactions.

Attributes:
    driver_wait (WebDriverWait): Common WebDriverWait instance to use
    in element searches.

"""
from lettuce import world
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def find_table_with_column_header(texts_headers):
    """Finds table with column headers that contain texts.

    Args:
        texts_headers (list): String in header texts.

    Returns:
        WebElement: Matched table.
    """
    table_xpath = '//table'

    for k in texts_headers:
        table_xpath += '//th[contains(., "%s")]/ancestor::table' % k
    table = find_element_by_xpath(table_xpath)
    return table


def find_row_contains(*row_contents):
    """Finds row with contents.

    Args:
        *row_contents (string): Strings contains in the result row.

    Returns:
        WebElement: Matched row.

    """
    contains_xpath = lambda text: '[contains(., "%s")]' % text
    xpath = '//tr'
    for content in row_contents:
        xpath += contains_xpath(content)
    xpath += '/td'
    return find_element_by_xpath(xpath)


def find_form():
    """Finds first occurence of form in page.

    Returns:
        WebElement: Matched form.

    """
    return find_element_by_tag_name('form')


def find_element_by_tag_name(tag_name):
    """Finds first occurence of ``tag_name`` element.

    Args:
        tag_name (string): Name of the html tag.

    Returns:
        WebElement: Matched element.

    """
    located = (By.TAG_NAME, tag_name)
    return world.wait.until(
        expected_conditions.visibility_of_element_located(located)
    )


def find_element_by_class(el_class):
    """Finds first occurence of element with class contains``el_class``.

    Args:
        el_class (string): Title of the class.

    Returns:
        WebElement: Matched element.

    """
    located = (By.CLASS_NAME, el_class)
    return world.wait.until(
        expected_conditions.visibility_of_element_located(located)
    )


def find_element_by_id(el_id):
    """Finds first occurence of any element with class contains``el_class``.

    Args:
        el_id (string): Title of the class.

    Returns:
        WebElement: Matched element.

    """
    located = (By.ID, el_id)
    return world.wait.until(
        expected_conditions.visibility_of_element_located(located)
    )


def find_select_by_name(select_name):
    el = find_element_by_name(select_name)
    return Select(el)


def find_element_by_name(field_name):
    """Finds element by name attribute value.

    Args:
        field_name (string): Name of the element.

    Returns:
        WebElement: Matched element.

    """
    located = (By.NAME, field_name)
    return world.wait.until(
        expected_conditions.visibility_of_element_located(located)
    )


def find_element_by_xpath(xpath, driver=None):
    """Finds element by xpath

    Returns:
        WebElement: Matched element.

    """
    if driver:
        local_wait = WebDriverWait(driver, world.wait._timeout)
    else:
        local_wait = world.wait
    located = (By.XPATH, xpath)
    return local_wait.until(
        expected_conditions.presence_of_element_located(located)
    )


def find_visible_element_by_xpath(xpath, driver=None):
    """Finds visible element by xpath

    Visibility means that the element is not only displayed
    but also has a height and width that is greater than 0.

    Returns:
        WebElement: Matched element.

    """
    if driver:
        local_wait = WebDriverWait(driver, world.wait._timeout)
    else:
        local_wait = world.wait
    located = (By.XPATH, xpath)
    return local_wait.until(
        expected_conditions.visibility_of_element_located(located)
    )


def find_clickable_element_by_xpath(xpath, driver=None):
    """Finds clickable element by xpath

    Returns:
        WebElement: Matched element.

    """
    if driver:
        local_wait = WebDriverWait(driver, world.wait._timeout)
    else:
        local_wait = world.wait
    located = (By.XPATH, xpath)
    return local_wait.until(
        expected_conditions.element_to_be_clickable(located)
    )


def find_clickable_element_by_id(element_id, driver=None):
    """Finds clickable element by id

    Returns:
        WebElement: Matched element.

    """
    if driver:
        local_wait = WebDriverWait(driver, world.wait._timeout)
    else:
        local_wait = world.wait
    located = (By.ID, element_id)
    return local_wait.until(
        expected_conditions.element_to_be_clickable(located)
    )


def find_elements_by_xpath(xpath, driver=None):
    """Finds multiple elements by xpath

    Returns:
        list: List of matched WebElements.

    """
    if driver:
        local_wait = WebDriverWait(driver, world.wait._timeout)
    else:
        local_wait = world.wait

    def get_elements(driver):
        elements = driver.find_elements_by_xpath(xpath)
        return elements if elements else False

    return local_wait.until(get_elements)


def find_link_by_text(text):
    """Finds link by text.

    Returns:
        WebElement: Matched link.

    """
    located = (By.LINK_TEXT, text)
    return world.wait.until(
        expected_conditions.visibility_of_element_located(located)
    )


def find_button_by_text(text):
    """Finds button by text.

    Returns:
        WebElement: Matched button.

    """
    xpath = '//button[contains(., "%s")]' % text
    return find_element_by_xpath(xpath)


def find_clickable_button_by_text(text):
    """Finds clickable button by text.

    Returns:
        WebElement: Matched button.

    """
    xpath = '//button[contains(., "%s")]' % text
    return find_clickable_element_by_xpath(xpath)


def find_invisible_element_by_xpath(xpath, driver=None):
    """Checks that an element is either invisible or not
    present on the DOM

    Returns Boolean value -- if element is displayed, then
    returns False
    In the case of NoSuchElement, returns true because the element is
    not present in DOM.
    In the case of StaleElementReference, returns true because stale
    element reference implies that element is no longer visible.
    """
    if driver:
        local_wait = WebDriverWait(driver, world.wait._timeout)
    else:
        local_wait = world.wait
    located = (By.XPATH, xpath)
    return local_wait.until(
        expected_conditions.invisibility_of_element_located(located)
    )


def find_invisible_element_by_id(element_id, driver=None):
    if driver:
        local_wait = WebDriverWait(driver, world.wait._timeout)
    else:
        local_wait = world.wait
    located = (By.ID, element_id)
    return local_wait.until(
        expected_conditions.invisibility_of_element_located(located)
    )
