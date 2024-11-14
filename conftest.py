import allure
import pytest
from allure_commons.types import AttachmentType

@pytest.fixture(scope="function", autouse=True)
def attach_screenshot(request):
    yield
    if request.node.rep_call.failed:
        try:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=AttachmentType.PNG
            )
        except Exception as e:
            print(f"Failed to attach screenshot: {e}")

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep
