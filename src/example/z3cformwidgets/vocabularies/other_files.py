# -*- coding: utf-8 -*-

from plone import api
from plone.app.vocabularies.catalog import CatalogSource
from zope.interface import implementer
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary


@implementer(IVocabularyFactory)
class OtherFiles(object):
    """
    """

    def __call__(self, context):
        return SimpleVocabulary.fromValues(['a', 'd', 'f'])


OtherFilesFactory = OtherFiles()


class CustomCatalogSource(CatalogSource):
    """
    """

    def __init__(self, context=None, **query):
        import pdb; pdb.set_trace()
        super(CustomCatalogSource, self).__init__(context, **query)


# CustomCatalogSourceFactory = CustomCatalogSource()
