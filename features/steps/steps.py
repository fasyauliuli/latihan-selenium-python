from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC

@given('I open the browser and go to "{url}"')
def open_browser(context, url):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.get(url)

@when('I search for "{query}"')
def search_google(context, query):
    search_box = context.driver.find_element(By.XPATH, "//textarea[@id='APjFqb']")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)

@then('I should see results related to "{query}"')
def verify_search_results(context, query):
    try:
        WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h3"))
        )
        assert query.lower() in context.driver.page_source.lower()
    finally:
        context.driver.quit()