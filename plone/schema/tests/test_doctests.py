""" Tests
"""
import unittest
import doctest


def test_suite():
    return unittest.TestSuite((
        doctest.DocTestSuite('plone.schema.jsonfield'),
    ))
