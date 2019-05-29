#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import unittest
import echo

to_upper = echo.to_upper
to_lower = echo.to_lower
to_title = echo.to_title
create_parser = echo.create_parser

# Your test case class goes here
class TestEcho(unittest.TestCase):
    def test_help(self):
        """ Running the program without arguments should show usage. """
        # Run the command `python ./echo.py -h` in a separate process, then
        # collect it's output.
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        stdout = stdout.decode('utf-8')

        with open("./USAGE", "r") as f:
            usage = f.read()

        self.assertEqual(len(stdout), len(usage))
        self.assertEqual(stdout, usage)


    def test_upper(self):
        self.assertEqual(to_upper('hello'), 'HELLO')
        self.assertEqual(to_upper('Hey'), 'HEY')
        self.assertEqual(to_upper('tEsTinG'), 'TESTING')

    
    def test_lower(self):
        self.assertEqual(to_lower('HELLO'), 'hello')
        self.assertEqual(to_lower('Hello'), 'hello')
        self.assertEqual(to_lower('tEsTinG'), 'testing')


    def test_title(self):
        self.assertEqual(to_title('HELLO'), 'Hello')
        self.assertEqual(to_title('hello'), 'Hello')
        self.assertEqual(to_title('tEsTinG'), 'Testing')

    def test_parser(self):
        parser = create_parser()
        arg_list = ['-ult', 'hello']

        name_space = parser.parse_args(arg_list)

        self.assertTrue(name_space.upper)
        self.assertTrue(name_space.lower)
        self.assertTrue(name_space.title)


if __name__ == '__main__':
    unittest.main()
