import unittest
import io
from contextlib import redirect_stdout

from helloworld import hello


class TestHelloWorld(unittest.TestCase):

    def test_hello(self):
        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            hello()
        self.assertEqual('Hello World!\n', captured_output.getvalue())


if __name__ == '__main__':
    unittest.main()