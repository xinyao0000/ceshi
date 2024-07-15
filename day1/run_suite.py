import unittest
from htmltestreport import HTMLTestReport

from day1.py10_unittest_demo import TestAdd

suite = unittest.TestSuite()

loader = unittest.TestLoader()

suite.addTest(loader.loadTestsFromTestCase(TestAdd))

ruuner = HTMLTestReport("测试报告.html")

ruuner.run(suite)