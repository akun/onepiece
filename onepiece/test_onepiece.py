#!/usr/bin/env python

from unittest import TestCase

from onepiece.main import hello_world


class HelloWordTestCase(TestCase):

    def test_hello_world(self):
        self.assertEqual('One Piece', hello_world())
