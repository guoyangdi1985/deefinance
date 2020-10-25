from django.core.management.base import BaseCommand, CommandError
from webauto.models import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import time


class Command(BaseCommand):
    help = 'Automation 100%. This is a selenium automation for town of Apex bill payment for electric' \
           'and water utilities.'
    BROWSER_DRIVER_PATH = 'D:\djangoprojects\deefinance\chromedriver'
    TOWN_OF_APEX_LOGIN_PAGE = 'https://secure.apexnc.org/eSuite.Utilities/default.aspx'

    def handle(self, *args, **options):
        # Load the browser driver.
        browser = webdriver.Chrome(self.BROWSER_DRIVER_PATH)
        # Go to town of Apex login page.
        browser.get(self.TOWN_OF_APEX_LOGIN_PAGE)
        username_textfield = browser.find_element_by_id('ctl00_ctl00_Content_MainContentPlaceHolder_uxUserName')
        password_textfield = browser.find_element_by_id('ctl00_ctl00_Content_MainContentPlaceHolder_uxPassword')
        credential = Credential.objects.get(payment_of_credential='town_of_apex')
        username_textfield.send_keys(credential.username)
        password_textfield.send_keys(credential.password)
        time.sleep(2)
        password_textfield.send_keys(Keys.ENTER)
        time.sleep(5)
        # Start making a payment.
        make_a_payment_hyperlink = browser.find_element_by_id('ctl00_ctl00_Content_MainContentPlaceHolder_uxStandardSummary_uxMakePayment')
        make_a_payment_hyperlink.click()
        time.sleep(5)
        # Start filling the form.
        credit_card = CreditCard.objects.get(id=1)
        # Personal information
        first_name_field = browser.find_element_by_id('ctl00_ctl00_Content_MainContentPlaceHolder_uxFirstName')
        last_name_field = browser.find_element_by_id('ctl00_ctl00_Content_MainContentPlaceHolder_uxLastName')
        # Extract card holder first name and last name.
        first_name, last_name = credit_card.card_holder_name.split(' ')
        first_name_field.send_keys(first_name)
        last_name_field.send_keys(last_name)
        street_address, city, state, zip_code = credit_card.billing_address.split(', ')
        address_field = browser.find_element_by_id('ctl00_ctl00_Content_MainContentPlaceHolder_uxStreetAddress')
        address_field.send_keys(street_address)
        city_field = browser.find_element_by_id('ctl00_ctl00_Content_MainContentPlaceHolder_uxCity')
        city_field.send_keys(city)
        state_dropdown = browser.find_element_by_id('ctl00_ctl00_Content_MainContentPlaceHolder_uxStateList')
        state_option = Select(state_dropdown)
        state_option.select_by_visible_text('NC')
        zip_code_field = browser.find_element_by_id('ctl00_ctl00_Content_MainContentPlaceHolder_uxZipcode')
        zip_code_field.send_keys(zip_code)
        # credit card information
        credit_card_type_dropdown = browser.find_element_by_id('ctl00_ctl00_Content_MainContentPlaceHolder_uxAcceptedCardTypeList')
        card_type_option = Select(credit_card_type_dropdown)
        card_type_option.select_by_visible_text('Visa')
        card_number_field = browser.find_element_by_id('ctl00_ctl00_Content_MainContentPlaceHolder_uxCardNumber')
        card_number_field.send_keys(credit_card.card_number.replace(' ', ''))
        expiration_month_dropdown = browser.find_element_by_id('ctl00_ctl00_Content_MainContentPlaceHolder_uxExpirationMonthList')
        month_option = Select(expiration_month_dropdown)
        month_option.select_by_visible_text('May')
        expiration_year_dropdown = browser.find_element_by_id('ctl00_ctl00_Content_MainContentPlaceHolder_uxExpirationYearList')
        year_option = Select(expiration_year_dropdown)
        year_option.select_by_visible_text('2023')
        security_code_field = browser.find_element_by_id('ctl00_ctl00_Content_MainContentPlaceHolder_uxCardSecurityCode')
        security_code_field.send_keys(credit_card.security_code)
        i_agree_checkbox = browser.find_element_by_id('ctl00_ctl00_Content_MainContentPlaceHolder_uxTermsAndConditions')
        i_agree_checkbox.click()
        # Click on complete payment button
        complete_payment_bt = browser.find_element_by_id('ctl00_ctl00_Content_MainContentPlaceHolder_uxSubmitPayment')
        time.sleep(5)
        complete_payment_bt.click()
        time.sleep(10)
        self.stdout.write(self.style.SUCCESS('Done!'))
