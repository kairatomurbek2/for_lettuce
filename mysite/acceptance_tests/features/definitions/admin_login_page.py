# -*- coding: utf-8 -*-
from lettuce import step
from acceptance_tests.features.definitions.core.common_actions import (
    admin_logs_in
)


@step(u'Я нахожусь в админ панель и логинюсь')
def i_am_admin_panel_and_login(step):
    admin_logs_in()
