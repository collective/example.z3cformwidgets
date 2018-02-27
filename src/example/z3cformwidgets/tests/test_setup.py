# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from example.z3cformwidgets.testing import EXAMPLE_Z3CFORMWIDGETS_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that example.z3cformwidgets is properly installed."""

    layer = EXAMPLE_Z3CFORMWIDGETS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if example.z3cformwidgets is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'example.z3cformwidgets'))

    def test_browserlayer(self):
        """Test that IExampleZ3CformwidgetsLayer is registered."""
        from example.z3cformwidgets.interfaces import (
            IExampleZ3CformwidgetsLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IExampleZ3CformwidgetsLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = EXAMPLE_Z3CFORMWIDGETS_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get(userid=TEST_USER_ID).getRoles()
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['example.z3cformwidgets'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if example.z3cformwidgets is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'example.z3cformwidgets'))

    def test_browserlayer_removed(self):
        """Test that IExampleZ3CformwidgetsLayer is removed."""
        from example.z3cformwidgets.interfaces import \
            IExampleZ3CformwidgetsLayer
        from plone.browserlayer import utils
        self.assertNotIn(
           IExampleZ3CformwidgetsLayer,
           utils.registered_layers())
