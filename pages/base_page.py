
from utils.wait_engine import WaitEngine


class BasePage:

    def __init__(self, page):
        self.page = page

    def click(self, locator):
        locator.click()
        WaitEngine.smart_wait(self.page)

    def fill(self, locator, value):
        locator.fill(value)

    def press_enter(self, locator):
        locator.press("Enter")

    def wait_for_page_load(self):
        self.page.wait_for_load_state(
            "networkidle"
        )

    def smart_wait(self):
        WaitEngine.smart_wait(
            self.page
        )
