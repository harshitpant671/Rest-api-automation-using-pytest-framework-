import pytest
import json
import os
from datetime import datetime

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    report_dir = 'reports'
    now= datetime.now().strftime("%y-%m-%d_%H-%M-%S")
    config.option.htmlpath = f"{report_dir}/report_{now}.html"

@pytest.fixture(scope = "session", autouse = True)
def setup_teardown():
    print("\nSetting up resource...")
    yield
    print("\nTearing down resources...")

@pytest.fixture
def load_user_data():
    json_file_path = os.path.json(os.path.dirname(__file__),"data","test_data.json")
    with open(json_file_path) as json_file:
        data = json.load(json_file)
    return data