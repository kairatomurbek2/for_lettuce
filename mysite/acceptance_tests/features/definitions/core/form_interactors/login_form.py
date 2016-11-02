from acceptance_tests.features.definitions.core.form_interactors._browser_interactor import (
    enter_into_field, submit_form
)


def enter_username(username):
    enter_into_field(field_name='username', text=username)


def enter_password(password):
    enter_into_field(field_name='password', text=password)


def submit():
    submit_form()
