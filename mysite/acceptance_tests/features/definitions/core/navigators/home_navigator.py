# -*- coding: utf-8 -*-
from acceptance_tests.features.definitions.core.navigators import _common


def go_to_home_page():
    _common.go_to_url('/')


def go_to_login_page():
    _common.go_to_url('/accounts/login')
