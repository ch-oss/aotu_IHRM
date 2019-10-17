#导包
import time
import unittest
from BeautifulReport import BeautifulReport

from case.test_case import TestIhrm

suite = unittest.TestSuite()

suite.addTest(unittest.makeSuite(TestIhrm))
# report_name = time.strftime("%Y%m%d%H%M%S")

BeautifulReport(suite).report\
    (description="chorm",filename="my_report.html",log_path="./report")