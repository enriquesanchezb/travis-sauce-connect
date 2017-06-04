from lettuce import before, world
from selenium import webdriver
import lettuce_webdriver.webdriver

@before.all
def setup_browser():
	desired_cap = {
	    'platform': "Mac OS X 10.9",
	    'browserName': "chrome",
	    'version': "31",
	}
	world.browser = webdriver.Remote(
		desired_capabilities=desired_cap,
		command_executor="http://enrisanbe:d7bbcdbd-e887-492a-88f8-82bd13151e47@ondemand.saucelabs.com:80/wd/hub"
	)
