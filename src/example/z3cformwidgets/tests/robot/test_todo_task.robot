# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s example.z3cformwidgets -t test_todo_task.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src example.z3cformwidgets.testing.EXAMPLE_Z3CFORMWIDGETS_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/plonetraining/testing/tests/robot/test_todo_task.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a todo_task
  Given a logged-in site administrator
    and an add todo_task form
   When I type 'My Todo Task' into the title field
    and I submit the form
   Then a todo_task with the title 'My Todo Task' has been created

Scenario: As a site administrator I can view a todo_task
  Given a logged-in site administrator
    and a todo_task 'My Todo Task'
   When I go to the todo_task view
   Then I can see the todo_task title 'My Todo Task'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add todo_task form
  Go To  ${PLONE_URL}/++add++todo_task

a todo_task 'My Todo Task'
  Create content  type=todo_task  id=my-todo_task  title=My Todo Task


# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IDublinCore.title  ${title}

I submit the form
  Click Button  Save

I go to the todo_task view
  Go To  ${PLONE_URL}/my-todo_task
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a todo_task with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the todo_task title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
