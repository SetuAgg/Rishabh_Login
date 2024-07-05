import pytest
from selenium import webdriver
from pytest_metadata.plugin import metadata_key
@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    return driver

def pytest_configure(config):
    config.stash[metadata_key] ['Project Name'] = 'Learning, MyProject'
    config.stash[metadata_key]['Test Module Name'] = 'Admin Login Tests'
    config.stash[metadata_key]['Tester Name'] = 'Setu Aggarwal'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('Plugins',None)
