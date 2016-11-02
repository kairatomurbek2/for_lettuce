"""
This module contains common assertion functions.
"""

from acceptance_tests.features.definitions.core import finder


def assert_row_exists_in_table(data):
    """
    Asserts existence of a table row with given data.

    If there are no any html elements appropriate to data, then
    raises an exception.

    Args:
        data (dict): data expected in row. Keys represent column
                     headers'(th) texts and values represent row(tr)
                     texts in corresponding columns(td).

    Examples:
        Suppose we have html table
        <table>
            <tr>
                <th>#</th>
                <th>Name</th>
                <th>Age</th>
            </tr>
            <tr>
                <td>1</td>
                <td>Alice</td>
                <td>22</td>
            </tr>
            <tr>
                <td>2</td>
                <td>Bob</td>
                <td>40</td>
            </tr>
        </table>

        >>> assert_row_exists_in_table({'Name': 'Alice', 'Age': 22})
        >>> assert_row_exists_in_table({'Name': 'Alice', 'Age': 33})
        ...TimeoutException
        >>> assert_row_exists_in_table({'#': 2, 'Name': 'Alice', 'Age': 22})
        ...TimeoutException
    """

    headers_texts = data.keys()
    headers_positioins = _get_header_positions(headers_texts)

    row_xpath = '//table//tr'
    contains_column = lambda order, value: '[contains(.//td[%s], "%s")]' % (order, value)
    for k in data:
        row_xpath += contains_column(headers_positioins[k], data[k])

    finder.find_element_by_xpath(row_xpath)


def _get_header_positions(texts_in_headers):
    """
    Finds position of headers in a table contains them.

    Args:
        texts_in_headers (list): List of strings contain in headers.

    Returns:
        dict: Pair of header texts and corresponding positions.
    """
    table = finder.find_table_with_column_header(texts_in_headers)

    column_headers = finder.find_elements_by_xpath('//th', table)

    headers_positions = {}
    current_position = 1
    for header in column_headers:
        if header.text in texts_in_headers:
            headers_positions[header.text] = current_position
        current_position += 1

    return headers_positions


def assert_last_table_row_has_column_with_text(column_index, text):
    """
    Checks whether column(td) of the last row(tr) contains ``text``
    and raises exception if does not.

    Look at last rows of all tables in the page.

    Args:
        column_index (int): Column(td) index in the last row of a table.
        text (string): Text in the column.
    """
    xpath = '//table//tr[last()][contains(./td[%s], "%s")]' % (column_index, text)
    finder.find_element_by_xpath(xpath)


def assert_text_is_displayed(text):
    xpath = '//*[contains(., "%s")]' % text
    finder.find_element_by_xpath(xpath)


def assert_error_alert_is_displayed(text):
    xpath = '//div[contains(@class, "alert") and contains(@class, "alert-danger") and contains(., "%s")]' % text
    finder.find_element_by_xpath(xpath)


def assert_info_alert_is_displayed(text):
    xpath = '//div[contains(@class, "alert") and contains(@class, "alert-success") and contains(., "%s")]' % text
    finder.find_visible_element_by_xpath(xpath)


def assert_element_is_invisible_by_xpath(xpath):
    finder.find_invisible_element_by_xpath(xpath)


def assert_element_is_invisible_by_id(element_id):
    finder.find_invisible_element_by_id(element_id)
