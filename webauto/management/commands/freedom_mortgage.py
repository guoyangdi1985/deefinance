from django.core.management.base import BaseCommand, CommandError
from webauto.models import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import time


class Command(BaseCommand):
    help = 'Automation 100%. This is a selenium automation for City of Raleigh utility bill payment.'
    BROWSER_DRIVER_PATH = 'D:\djangoprojects\deefinance\chromedriver'
    CITY_OF_RALEIGH_LOGIN_PAGE = 'https://myaccount.freedommortgage.com/'

    def handle(self, *args, **options):
        # Load the browser driver.
        browser = webdriver.Chrome(self.BROWSER_DRIVER_PATH)
        # Go to freedom mortgage login page.
        browser.get(self.CITY_OF_RALEIGH_LOGIN_PAGE)
        credential = Credential.objects.get(payment_of_credential='freedom mortgage')
        username_field = browser.find_element_by_id('login_userName')
        username_field.send_keys(credential.username)
        password_field = browser.find_element_by_id('login_password')
        password_field.send_keys(credential.password)
        password_field.send_keys(Keys.ENTER)
        paynow_btn = browser.find_element_by_link_text('One Time Payment')
        paynow_btn.click()
        time.sleep(5)
        account_type_dropdown = browser.find_element_by_id('select_8')
        account_type_dropdown.click()
        time.sleep(2)
        checking_option = browser.find_element_by_id('select_option_17')
        checking_option.click()

        bank = credential.bankdrafts.get(bank_name='bank of america')
        acct_num_field = browser.find_element_by_id('input_10')
        acct_num_field.send_keys(bank.account_number)
        acct_num_field.send_keys(Keys.TAB)
        time.sleep(2)
        acct_num_field_confirm = browser.find_element_by_id('input_301')
        acct_num_field_confirm.send_keys(bank.account_number)
        acct_num_field.send_keys(Keys.ENTER)
        time.sleep(2)
        routing_num_field = browser.find_element_by_id('input_236')
        routing_num_field.send_keys(bank.routing_number)
        name_on_acct_field = browser.find_element_by_id('input_237')
        name_on_acct_field.send_keys(bank.account_hold_name)


        self.stdout.write(self.style.SUCCESS('Complete!!!!'))
