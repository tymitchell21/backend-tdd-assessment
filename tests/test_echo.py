#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from echo import echo

# Your test case class goes here
class TestEcho(unittest.TestCase):
    def test_echo(self):
        self.assertEqual(echo('hey'), 'hey')
        self.assertNotEqual(echo('yo'), 'hello')


if __name__ == '__main__':
    unittest.main()
