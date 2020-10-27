from django.core.management.base import BaseCommand, CommandError
from webauto.models import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time


class Command(BaseCommand):
    help = 'Automation 90%. This is a selenium automation for spectrum bill payment.'
    BROWSER_DRIVER_PATH = 'D:\djangoprojects\deefinance\chromedriver'
    SPECTRUM_LOGIN_PAGE = 'https://www.spectrum.net/login'

    def handle(self, *args, **options):
        # Load the browser driver.
        browser = webdriver.Chrome(self.BROWSER_DRIVER_PATH)
        # Go to spectrum login page.
        browser.get(self.SPECTRUM_LOGIN_PAGE)
        # Find the remember me checkout and uncheck it.
        checkbox = browser.find_element_by_class_name('kite-custom-control-indicator')
        checkbox.click()
        # Type in username and password.
        username_bt = browser.find_element_by_id('cc-username')
        pasword_bt = browser.find_element_by_id('cc-user-password')
        credential = Credential.objects.get(payment_of_credential='spectrum')
        username_bt.send_keys(credential.username)
        pasword_bt.send_keys(credential.password)
        pasword_bt.send_keys(Keys.ENTER)
        time.sleep(5)

        payment_bt = browser.find_element_by_xpath(
            '//*[@id="billing-summary-container"]/spectrum-dynamic-fixed-card/div/div[4]/div[2]/div[3]/div[2]/div/button')
        payment_bt.click()

        continue_bt = browser.find_element_by_xpath(
            '//*[@id="spectrum-container"]/main/spectrum-billing/div[3]/div/div[2]/billing-one-time-payment/spectrum-expansion-card/spectrum-card/ngk-typography/ngk-card/div/div[4]/spectrum-expansion-card-content/form/billing-payment-amount/spectrum-accordion-panel/div[2]/spectrum-accordion-panel-action-row/app-button-row/div/button')
        continue_bt.click()

        continue_payment_bt = browser.find_element_by_xpath(
            '//*[@id="spectrum-container"]/main/spectrum-billing/div[3]/div/div[2]/billing-one-time-payment/spectrum-expansion-card/spectrum-card/ngk-typography/ngk-card/div/div[4]/spectrum-expansion-card-content/form/billing-payment-date/spectrum-accordion-panel/div[2]/spectrum-accordion-panel-action-row/app-button-row/div/button[2]')
        continue_payment_bt.click()

        time.sleep(30)

        self.stdout.write(self.style.SUCCESS('Testing!!!!'))
