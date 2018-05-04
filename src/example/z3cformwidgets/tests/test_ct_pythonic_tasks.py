# -*- coding: utf-8 -*-
from example.z3cformwidgets.content.pythonic_tasks import IPythonicTasks  # NOQA E501
from example.z3cformwidgets.testing import EXAMPLE_Z3CFORMWIDGETS_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest


try:
    from plone.dexterity.schema import portalTypeToSchemaName
except ImportError:
    # Plone < 5
    from plone.dexterity.utils import portalTypeToSchemaName


class PythonicTasksIntegrationTest(unittest.TestCase):

    layer = EXAMPLE_Z3CFORMWIDGETS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_ct_pythonic_tasks_schema(self):
        fti = queryUtility(IDexterityFTI, name='Pythonic Tasks')
        schema = fti.lookupSchema()
        self.assertEqual(IPythonicTasks, schema)

    def test_ct_pythonic_tasks_fti(self):
        fti = queryUtility(IDexterityFTI, name='Pythonic Tasks')
        self.assertTrue(fti)

    def test_ct_pythonic_tasks_factory(self):
        fti = queryUtility(IDexterityFTI, name='Pythonic Tasks')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IPythonicTasks.providedBy(obj),
            u'IPythonicTasks not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_pythonic_tasks_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='Pythonic Tasks',
            id='pythonic_tasks',
        )
        self.assertTrue(
            IPythonicTasks.providedBy(obj),
            u'IPythonicTasks not provided by {0}!'.format(
                obj.id,
            ),
        )
