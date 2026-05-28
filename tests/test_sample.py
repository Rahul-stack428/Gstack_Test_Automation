from playwright.sync_api import Playwright
from datetime import datetime
import pytest_playwright
import pytest
from datetime import datetime


def test_platform_creation(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://admin-test.granitestack.ai/admin/login")
    page.wait_for_timeout(5000)
    page.locator("input[name=\"email\"]").click()
    page.locator("input[name=\"email\"]").fill("rahul.ranjan@thoughts2binary.com")
    page.locator("input[name=\"password\"]").click()
    page.locator("input[name=\"password\"]").fill("Rahul@123")
    page.get_by_role("button", name="Sign In").click()
    page.get_by_text("Platform Admin").click()
    page.locator("button").filter(has_text="Rahul").click()
    page.get_by_role("button", name="G Gstack").click()
    page.get_by_role("button", name="Create New Project Start").click()
    page.locator("input[name=\"name\"]").click()
    unique_name = "user_" + datetime.now().strftime("%Y%m%d%H%M%S")
    page.locator("input[name=\"name\"]").fill(unique_name)
    page.locator("input[name=\"description\"]").click()
    page.locator("input[name=\"description\"]").fill("Test")
    page.get_by_role("button", name="Build from Scratch").click()
    page.locator("button[aria-label='Close']").click()
    page.get_by_placeholder("Enter Prompt Query").wait_for(state="visible")

    page.get_by_placeholder("Enter Prompt Query").fill("E-commerce platform")

    page.keyboard.press("Enter")
    page.wait_for_timeout(3000)
    page.locator("//button[@aria-label='Open Drop']").nth(4).click()
    page.get_by_role("button", name="Convert To Tenant Type").click()
    page.get_by_role("button", name="Yes").click()
    page.get_by_text("Yes").click()
    page.get_by_text("Deploy Beta").click()
    page.get_by_role("button", name="Yes").click()




