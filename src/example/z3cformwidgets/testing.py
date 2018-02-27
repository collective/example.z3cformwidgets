# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import example.z3cformwidgets


class ExampleZ3CformwidgetsLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=example.z3cformwidgets)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'example.z3cformwidgets:default')


EXAMPLE_Z3CFORMWIDGETS_FIXTURE = ExampleZ3CformwidgetsLayer()


EXAMPLE_Z3CFORMWIDGETS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(EXAMPLE_Z3CFORMWIDGETS_FIXTURE,),
    name='ExampleZ3CformwidgetsLayer:IntegrationTesting'
)


EXAMPLE_Z3CFORMWIDGETS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(EXAMPLE_Z3CFORMWIDGETS_FIXTURE,),
    name='ExampleZ3CformwidgetsLayer:FunctionalTesting'
)


EXAMPLE_Z3CFORMWIDGETS_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        EXAMPLE_Z3CFORMWIDGETS_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='ExampleZ3CformwidgetsLayer:AcceptanceTesting'
)
