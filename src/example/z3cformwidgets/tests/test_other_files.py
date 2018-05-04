# -*- coding: utf-8 -*-
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from example.z3cformwidgets.testing import EXAMPLE_Z3CFORMWIDGETS_INTEGRATION_TESTING  # noqa
from example.z3cformwidgets import _
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.interfaces import IVocabularyTokenized

import unittest


class OtherFilesIntegrationTest(unittest.TestCase):

    layer = EXAMPLE_Z3CFORMWIDGETS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_vocabulary(self):
        vocab_name = "example.z3cformwidgets.OtherFiles"
        factory = getUtility(IVocabularyFactory, vocab_name)
        self.assertTrue(IVocabularyFactory.providedBy(factory))

        vocabulary = factory(self.portal)
        self.assertTrue(IVocabularyTokenized.providedBy(vocabulary))
        self.assertEqual(
            vocabulary.getTerm('a').title,
            _(u'a'),
        )
