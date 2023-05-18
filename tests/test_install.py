import unittest
from subprocess import run


class TestInstall(unittest.TestCase):
    def test_library_installed(self):
        import quantready_base

        self.assertIsNotNone(quantready_base)

    def test_module(self):
        run(["python", "-m", "quantready_base", "--help"])

    def test_consolescript(self):
        run(["quantready-base", "--help"])
