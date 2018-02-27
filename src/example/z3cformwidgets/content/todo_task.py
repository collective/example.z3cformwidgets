# -*- coding: utf-8 -*-
from plone.dexterity.content import Item
from plone.supermodel import model
from plone import schema
from zope.interface import implementer, Interface
from example.z3cformwidgets import _


class INameTokenTableRowSchema(Interface):
    """Schema for dict rows used in DataGridFields.

    name is the 'real' name
    token is the token used in the vocabularies
    """
    token = schema.TextLine(title=_(u'Token'))
    name = schema.TextLine(title=_(u'Name'))


class ITodoTask(model.Schema):
    """ Marker interface for TodoTask
    """


@implementer(ITodoTask)
class TodoTask(Item):
    """
    """
