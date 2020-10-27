from django.core.management.base import BaseCommand, CommandError
from webauto.models import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import time


class Command(BaseCommand):
    help = 'Automation 90%. This is a selenium automation for spectrum bill payment.'
    BROWSER_DRIVER_PATH = 'D:\djangoprojects\deefinance\chromedriver'
    CITY_OF_RALEIGH_LOGIN_PAGE = 'https://ubwss.raleighnc.gov/login'

    def handle(self, *args, **options):
        # Load the browser driver.
        browser = webdriver.Chrome(self.BROWSER_DRIVER_PATH)
        # Go to City of Raleigh login page.
        browser.get(self.CITY_OF_RALEIGH_LOGIN_PAGE)
        credential = Credential.objects.get(payment_of_credential='city of raleigh')
        username_field = browser.find_element_by_id('userId')
        password_field = browser.find_element_by_id('password')
        username_field.send_keys(credential.username)
        password_field.send_keys(credential.password)
        time.sleep(2)
        password_field.send_keys(Keys.ENTER)
        time.sleep(5)
        # Start making a payment.
        pay_now_btn = browser.find_element_by_link_text('Pay Now')
        pay_now_btn.click()
        # Start filling the form.
        creditcard = credential.creditcards.get(id=2)
        creditCardNumber_field = browser.find_element_by_id('creditCardNumber')
        creditCardNumber_field.send_keys(creditcard.card_number.replace(' ', ''))
        expMonth_dropdown = browser.find_element_by_id('expMonth')
        expMonth_option = Select(expMonth_dropdown)
        creditcard_month, creditcard_year = creditcard.expiration.split('/')
        expMonth_option.select_by_visible_text(creditcard_month)
        expYear_dropdown = browser.find_element_by_id('expYear')
        expYear_option = Select(expYear_dropdown)
        expYear_option.select_by_visible_text('20' + creditcard_year)
        cvvNumber_field = browser.find_element_by_id('cvvNumber')
        cvvNumber_field.send_keys(creditcard.security_code)
        time.sleep(5)
        # Submit the payment.
        cvvNumber_field.send_keys(Keys.ENTER)
        time.sleep(3)
        # Paybutton
        paybutton = browser.find_element_by_id('Paybutton')
        paybutton.click()
        time.sleep(5)
        self.stdout.write(self.style.SUCCESS('Complete!!!!'))
