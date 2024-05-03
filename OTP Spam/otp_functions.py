from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def get_otp_rummy(phone_number, mobile_id, button_id, website_link):

    driver = webdriver.Chrome()
    try:
        # Go to the target website
        driver.get(website_link)

        # Wait for the phone number input field to be present and enter the phone number
        phone_number_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID,mobile_id))
        )
        phone_number_input.send_keys(phone_number)

        # Wait for the 'GET STARTED' button to be clickable and click it
        get_started_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, button_id))
        )
        get_started_button.click()
    
    except:
        print("The website with website link: ")
        print(website_link)
        print(" is not working")

    driver.quit()

def get_otp_2(phone_number, placeholder_text, button_name,  website_link):

    driver = webdriver.Chrome()
    try:
        # Go to the target website
        driver.get(website_link)

        # Wait for the phone number input field to be present and enter the phone number
        phone_number_input = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, f"//input[@placeholder='{placeholder_text}']")))
        phone_number_input.send_keys(phone_number)       


        # Wait for the 'GET STARTED' button to be clickable and click it
        get_started_button = WebDriverWait(driver, 10).until( EC.element_to_be_clickable((By.XPATH, f"//button[text()='{button_name}']")))    
        get_started_button.click()
    
    except:
        print("The website with website link: ")
        print(website_link)
        print(" is not working")

    driver.quit()
