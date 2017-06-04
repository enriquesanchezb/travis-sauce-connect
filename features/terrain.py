from lettuce import before, world
from selenium import webdriver
import lettuce_webdriver.webdriver

@before.all
def setup_browser():
    desired_capabilities = webdriver.DesiredCapabilities.FIREFOX
    desired_capabilities['version'] = 'latest'
    desired_capabilities['platform'] = 'WINDOWS'
    desired_capabilities['name'] = 'Testing Selenium with Lettuce'

    world.browser = webdriver.Remote(
        desired_capabilities=desired_capabilities,
        command_executor="http://enrisanbe:d7bbcdbd-e887-492a-88f8-82bd13151e47@ondemand.saucelabs.com:80/wd/hub',"
    )
