import os
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

load_dotenv()
HOME_URL = os.getenv("HOME_URL")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

def run(playwright):
    chromium = playwright.chromium
    browser = chromium.launch(headless=False, channel="chrome", args=[
                              "--start-fullscreen"])
    page = browser.new_page()
    page.goto(HOME_URL)
    page.set_viewport_size({"width": 2560, "height": 1440})
    # page.evaluate("() => { return window.outerWidth = screen.width; window.outerHeight = screen.height; }")
    
    cha = page.get_by_text("この画像に見える文字を入力してください").inner_text()
    
    if (cha == "この画像に見える文字を入力してください:"):
        print(cha)
        cha_input = page.get_by_placeholder("文字を入力してください")
        cha_input.focus()
        cha_input.press_sequentially("手动输入", delay=100)
        page.evaluate("window.x = 0; setTimeout(() => { window.x = 100 }, 5000);")
        page.wait_for_function("() => window.x > 0")
    login = page.get_by_role("link", name="您好,请登录 账户及心愿单")
    login.click()
    page.get_by_label("邮箱地址").press_sequentially(USERNAME, delay=100)
    page.get_by_label("继续").click()
    page.get_by_label("密码").press_sequentially(PASSWORD, delay=100)
    page.get_by_label("登录", exact=True).click()
    page.get_by_placeholder("搜索 Amazon.co.jp").press_sequentially("ランドセル", delay=100)
    page.get_by_role("button", name="搜索").click()
    print(page.url)
    page.goto(page.url + "&low-price=8000&high-price=30000")
    page.pause()
    # browser.close()

if __name__ == "__main__":
    with sync_playwright() as playwright:
        run(playwright)
