# -*- coding: utf-8 -*-
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from example.z3cformwidgets.content.todo_task import ITodoTask
from example.z3cformwidgets.testing import EXAMPLE_Z3CFORMWIDGETS_INTEGRATION_TESTING  # noqa
from zope.component import createObject
from zope.component import queryUtility

import unittest


class TodoTaskIntegrationTest(unittest.TestCase):

    layer = EXAMPLE_Z3CFORMWIDGETS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='todo_task')
        schema = fti.lookupSchema()
        schema_name = "plone_0_todo_task"
        self.assertEqual(schema_name, schema.getName())

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='todo_task')
        self.assertTrue(fti)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='todo_task')
        factory = fti.factory
        obj = createObject(factory)
        self.assertTrue(ITodoTask.providedBy(obj))

    def test_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='todo_task',
            id='todo_task',
        )
        self.assertTrue(ITodoTask.providedBy(obj))
