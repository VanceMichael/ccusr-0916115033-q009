import unittest
from app.db import upgrade
class DbTest(unittest.TestCase):
 def test_repeatable(self): upgrade(); upgrade()
