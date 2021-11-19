from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
 browser = p.chromium.launch(headless=False,slow_mo=50)
 page = browser.new_page()
 page.goto('https://app.apollo.io/#/login?redirectTo=https%3A%2F%2Fapp.apollo.io%2F%23%2F')
 page.click('div#provider-mounter')
 time.sleep(10)


 