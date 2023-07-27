import os
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

load_dotenv()
HOME_URL = os.getenv("HOME_URL")

def run(playwright):
    chromium = playwright.chromium
    browser = chromium.launch(headless=False, channel="chrome", args=[
                              "--start-fullscreen"])
    page = browser.new_page(no_viewport=True)
    page.goto(HOME_URL)
    page.set_viewport_size({"width": 3840, "height": 2160})
    # page.pause()
    # browser.close()

if __name__ == "__main__":
    with sync_playwright() as playwright:
        run(playwright)
