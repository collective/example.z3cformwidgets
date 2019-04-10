# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.autoform import directives
from plone.dexterity.content import Item
from plone.app.z3cform.widget import RelatedItemsFieldWidget
from plone.namedfile import field as namedfile
from plone.supermodel import model
from plone.supermodel.directives import fieldset
from z3c.relationfield.schema import RelationChoice
from z3c.relationfield.schema import RelationList
from z3c.form.browser.radio import RadioFieldWidget
from plone.app.vocabularies.catalog import CatalogSource
from zope import schema
from zope.interface import implementer
from example.z3cformwidgets import _


class IPythonicTasks(model.Schema):
    """ Marker interface and Dexterity Python Schema for PythonicTasks
    """
    directives.widget(
        'attachments',
        RelatedItemsFieldWidget,
    )
    attachments = RelationList(
        title=_(u'Attachments'),
        value_type=RelationChoice(
            title=_(u'Related'),
            source=CatalogSource(
                portal_type=['File'],
            ),
        ),
        required=False,
    )


@implementer(IPythonicTasks)
class PythonicTasks(Item):
    """
    """
