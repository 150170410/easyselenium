easyselenium
============

[![Build Status](https://travis-ci.org/kirillstrelkov/easyselenium.svg?branch=master)](https://travis-ci.org/kirillstrelkov/easyselenium)

Framework based on Selenium WebDriver. Contains wrapper around Selenium WebDriver functionaly and UI to facilitate in development.

Features:
* Supports Firefox, Chrome, IE, Opera and PhantomJS.
* Supports [PageObject pattern](https://code.google.com/p/selenium/wiki/PageObjects)
* Supports Continuous Integration
* Suits for novice users.
* Supports Python 2 and Python 3

Framework can be used as standalone framework with UI and/or as a library.
Supportive classes:
* [browser.py](/easyselenium/browser.py)
* [base_page_object.py](/easyselenium/base_page_object.py)
* [base_test.py](/easyselenium/base_test.py)

GUI [easy_selenium_ui.py](/easyselenium/scripts/easy_selenium_ui.py):
* Generator
* Editor
* Test runner

Dependencies
------------
1. Python
2. wxPython
3. Selenium WebDriver
4. nose
 1. nose-htmloutput plug-in
 2. nose-pathmunge plug-in

Simple usage
-----
Most of `Browser` functions support both `WebElement` object and tuple/list which represents html element. This tuple/list object should contain selector/locator as first element and value as a second element. Example: `input = (By.NAME, 'q')`

Here is simple example: 
```python
>>> from selenium.webdriver.common.by import By
>>> from easyselenium.browser import Browser
>>> browser = Browser('ff') # initilizing browser
>>> browser.get('http://www.google.com') # going to google
>>> # creating variables for page elements:
>>> input = (By.NAME, 'q') # input element
>>> search_btn = (By.NAME, 'btnG') # search button element
>>> result = (By.CSS_SELECTOR, '.r') # found results titles' elements
>>> # back to action
>>> browser.type(input, u'selenium') # typing 'selenium' into search field
>>> browser.click(search_btn) # clicking search button
>>> browser.get_text(result) # getting first found title
u'Selenium - Web Browser Automation'
>>> browser.quit() # closing browser
```

Check [browser_test.py](/easyselenium/test/browser_test.py) for more examples.

Continuous Integration
----------------------
Done via command line script [easy_selenium_cli.py](/easyselenium/scripts/easy_selenium_cli.py)

Installation
------------
1. Download latest code from GitHub
2. Extract it
3. Open terminal or command line console
4. Navigate to extracted folder
5. Install all required libraries
```shell
python -m pip install -r requirements.txt
```
5. Go to `easyselenium` folder and install with command:
```shell
python setup.py install
```

License
-------
MIT License [easyselenium_license.txt](/easyselenium/licenses/easyselenium_license.txt)

Tutorial
--------
1. [Introduction](https://kirillstrelkov.blogspot.de/2016/03/test-automation-with-selenium-webdriver.html)
2. [Setup](https://kirillstrelkov.blogspot.de/2016/03/test-automation-with-selenium-webdriver_28.html)
3. [Test creation](https://kirillstrelkov.blogspot.de/2016/03/test-automation-tutorial-with-selenium.html)
4. [Continuous Integration](https://kirillstrelkov.blogspot.com/2018/04/test-automation-tutorial-with-selenium.html)

More information
----------------
[Presentation](https://www.dropbox.com/s/4y877giru9qwx3b/present_Kirill_Strelkov.pdf?dl=0)

[Thesis which contains description of the framework](https://www.dropbox.com/s/l65o69wvzjf1bue/Kirill_Strelkov_073639_BAK.pdf?dl=0)
