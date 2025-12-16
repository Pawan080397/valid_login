import pytest
import os
from datetime import datetime

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call":
        driver = item.funcargs.get("driver", None)
        if driver is None:
            return

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        if rep.outcome == "passed":
            folder = "screenshots/pass"
        else:
            folder = "screenshots/fail"

        os.makedirs(folder, exist_ok=True)
        screenshot_path = f"{folder}/{item.name}_{timestamp}.png"
        driver.save_screenshot(screenshot_path)

        # HTML report attachment
        if hasattr(rep, "extra"):
            extra = rep.extra
        else:
            extra = []

        extra.append(pytest_html.extras.image(screenshot_path))
        rep.extra = extra


def pytest_configure(config):
    global pytest_html
    pytest_html = config.pluginmanager.getplugin("html")
