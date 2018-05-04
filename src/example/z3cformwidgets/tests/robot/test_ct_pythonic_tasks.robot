# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s example.z3cformwidgets -t test_pythonic_tasks.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src example.z3cformwidgets.testing.EXAMPLE_Z3CFORMWIDGETS_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/plonetraining/testing/tests/robot/test_pythonic_tasks.robot
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

Scenario: As a site administrator I can add a Pythonic Tasks
  Given a logged-in site administrator
    and an add Pythonic Tasks form
   When I type 'My Pythonic Tasks' into the title field
    and I submit the form
   Then a Pythonic Tasks with the title 'My Pythonic Tasks' has been created

Scenario: As a site administrator I can view a Pythonic Tasks
  Given a logged-in site administrator
    and a Pythonic Tasks 'My Pythonic Tasks'
   When I go to the Pythonic Tasks view
   Then I can see the Pythonic Tasks title 'My Pythonic Tasks'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Pythonic Tasks form
  Go To  ${PLONE_URL}/++add++Pythonic Tasks

a Pythonic Tasks 'My Pythonic Tasks'
  Create content  type=Pythonic Tasks  id=my-pythonic_tasks  title=My Pythonic Tasks


# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form-widgets-IBasic-title  ${title}

I submit the form
  Click Button  Save

I go to the Pythonic Tasks view
  Go To  ${PLONE_URL}/my-pythonic_tasks
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Pythonic Tasks with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Pythonic Tasks title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
