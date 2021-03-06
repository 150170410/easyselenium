# coding=utf8
import traceback

from nose.result import TextTestResult
from unittest.case import TestCase

from easyselenium.browser import Browser
from easyselenium.utils import Logger, get_timestamp


class BaseTest(TestCase):
    TC_NAME_WIDTH = 100
    BROWSER_NAME = None
    FAILED_SCREENSHOT_FOLDER = None
    logger = Logger(name='easyselenim.base_test.BaseTest')

    @classmethod
    def setUpClass(cls):
        super(BaseTest, cls).setUpClass()
        if cls.BROWSER_NAME and not Browser.DEFAULT_BROWSER:
            Browser.DEFAULT_BROWSER = cls.BROWSER_NAME
        cls.browser = Browser(logger=cls.logger)

    @classmethod
    def tearDownClass(cls):
        super(BaseTest, cls).tearDownClass()
        cls.browser.quit()

    def setUp(self):
        TestCase.setUp(self)
        if self.browser.logger:
            name = self.id()
            symbols_before = u'-' * int((self.TC_NAME_WIDTH - len(name) - 2) / 2)
            self.browser.logger.info('{} {} {}'.format(symbols_before, name, symbols_before))

    def tearDown(self):
        failed = True
        if hasattr(self, '_outcome'):
            # python3
            failed = not self._outcome.success
        elif hasattr(self, '_resultForDoCleanups') and hasattr(self._resultForDoCleanups, 'result'):
            # nose
            failed = not self._resultForDoCleanups.result.wasSuccessful()
        elif hasattr(self, '_resultForDoCleanups') and hasattr(self._resultForDoCleanups, 'current_failed'):
            # python2
            failed = self._resultForDoCleanups.current_failed

        if failed:
            name = self.id()
            filename = u'_'.join([name,
                                  self.browser.get_browser_initials(),
                                  get_timestamp()])
            try:
                self.browser.save_screenshot(self.FAILED_SCREENSHOT_FOLDER,
                                             filename + u'.png')
            except Exception:
                formatted_exc = traceback.format_exc()
                self.browser.logger.info(formatted_exc)
        TestCase.tearDown(self)

        if self.browser.logger:
            self.browser.logger.info(u"-" * self.TC_NAME_WIDTH)
