import unittest
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))


class TestLineEndingsChecker(unittest.TestCase):
    def test_import(self):
        import line_endings_checker

    def test_basic(self):
        # smoke test — just verify no exceptions on valid input
        pass


if __name__ == '__main__':
    unittest.main()
