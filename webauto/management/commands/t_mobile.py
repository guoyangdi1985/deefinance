from django.core.management.base import BaseCommand, CommandError
from webauto.models import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import time


class Command(BaseCommand):
    help = 'Automation 80%. This is a selenium automation for Dominion Energy Gas bill payment.'
    BROWSER_DRIVER_PATH = 'D:\djangoprojects\deefinance\chromedriver'
    T_MOBILE_LOGIN_PAGE = 'https://account.t-mobile.com/signin/v2/?redirect_uri=https:%2F%2Fwww.t-mobile.com%2F' \
                                 'signin&scope=TMO_ID_profile%2520associated_lines%2520billing_information%2520' \
                                 'associated_billing_accounts%2520extended_lines%2520token%2520openid%2520vault&' \
                                 'client_id=MYTMO&access_type=ONLINE&response_type=code&approval_prompt=auto&' \
                                 'prompt=select_account&state=eyJpbnRlbnQiOiJMb2dpbiIsImJvb2ttYXJrVXJsIjoiaHR0cHM6Ly' \
                                 '9teS50LW1vYmlsZS5jb20ifQ'

    def handle(self, *args, **options):
        # Load the browser driver.
        browser = webdriver.Chrome(self.BROWSER_DRIVER_PATH)
        # Go to Dominion Energy login page.
        browser.get(self.T_MOBILE_LOGIN_PAGE)
        time.sleep(3)
        credential = Credential.objects.get(payment_of_credential='t mobile')
        username_field = browser.find_element_by_id('usernameTextBox')
        username_field.send_keys(credential.username)
        username_field.send_keys(Keys.ENTER)
        time.sleep(3)
        next_btn = browser.find_element_by_id('lp1-next-btn')
        next_btn.click()




        self.stdout.write(self.style.SUCCESS('Complete!!!!'))
