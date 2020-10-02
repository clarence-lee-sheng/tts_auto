from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

PATH = "C:\Program Files (x86)\chromedriver.exe"

username = "student id here "
password = "password here"

driver = webdriver.Chrome(PATH)

driver.get("https://tts.sutd.edu.sg")

username_input = driver.find_element_by_name("ctl00$pgContent1$uiLoginid")
username_input.send_keys(username)

password_input = driver.find_element_by_name("ctl00$pgContent1$uiPassword")
password_input.send_keys(password)

username_input.send_keys(Keys.RETURN)

temperature_site_link = driver.find_element_by_link_text("Temperature Taking")
temperature_site_link.click()

window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
temperature_select = driver.find_element_by_id("pgContent1_uiTemperature")

all_options = temperature_select.find_elements_by_tag_name("option")
for option in all_options:
    value = option.get_attribute("value")
    if value == "Less than or equal to 37.6°C":
        option.click()

temperature_submit_button = driver.find_element_by_id("pgContent1_btnSave")
temperature_submit_button.click()
driver.switch_to.alert.accept()

window_before = driver.window_handles[0]
driver.switch_to.window(window_before)

daily_declaration_link = driver.find_element_by_link_text("Daily Declaration")
daily_declaration_link.click()

window_after = driver.window_handles[2]
driver.switch_to.window(window_after)

travelled_to_other_countries_no_button = driver.find_element_by_id("pgContent1_rbVisitOtherCountryNo")
travelled_to_other_countries_no_button.click()

quarantine_no_button = driver.find_element_by_id("pgContent1_rbNoticeNo")
quarantine_no_button.click()

shn_no_button = driver.find_element_by_id("pgContent1_rbContactNo")
shn_no_button.click()

mc_no_button = driver.find_element_by_id("pgContent1_rbMCNo")
mc_no_button.click()

daily_declaration_submit_button = driver.find_element_by_id("pgContent1_btnSave")
daily_declaration_submit_button.click()
driver.switch_to.alert.accept()

driver.quit()