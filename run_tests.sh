#!/bin/bash

. virtualenv/bin/activate
cd mysite
# unit tests
#./manage.py test acceptance_tests --settings=main.settings_unit_test --noinput


# acceptance tests
RUN_TEST_COMMAND="./manage.py harvest acceptance_tests/features --settings=main.settings_test --debug-mode"
for var in ${@}
do
    RUN_TEST_COMMAND=${RUN_TEST_COMMAND}" -t ${var}"
done
bash -c "${RUN_TEST_COMMAND}"
deactivate