# -*- coding: utf-8 -*-
from unittest import TestCase

from nose.tools import assert_raises
from messytables import DateType


class TestDateType(TestCase):
    def test_initialization(self):
        assert_raises(ValueError, DateType, 'Not-a-valid-date-format')
