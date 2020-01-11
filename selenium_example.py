#Alexandro Marcelo Gonzalez A01021383
#Running in firefox using python3
from selenium import webdriver
import datetime

browser = webdriver.Firefox(executable_path=r'./geckodriver')
#browser = webdriver.Safari(executable_path=r'/usr/bin/safaridriver')
browser.get('http://a.testaddressbook.com')

log_in= browser.find_element_by_id('sign-in')
log_in.click()
mail= browser.find_element_by_id('session_email')
mail.send_keys('watir_example@example.com')
password = browser.find_element_by_id('session_password') 
password.send_keys('password')
btn = browser.find_element_by_name('commit').click()

addresses = browser.find_element_by_link_text('Addresses')
addresses.click()
browser.get('http://a.testaddressbook.com/addresses/new')


browser.find_element_by_id('address_first_name').send_keys('Alex')
browser.find_element_by_id('address_last_name').send_keys('MMMMMMM')
browser.find_element_by_id('address_street_address').send_keys('Av. Carlos Lazo')
browser.find_element_by_id('address_secondary_address').send_keys('Av. Tamaulipas')
browser.find_element_by_id('address_city').send_keys('Ciudad de Mexico')
browser.find_element_by_id('address_state').send_keys('Nevada')
browser.find_element_by_id('address_zip_code').send_keys('05000')
browser.find_element_by_id('address_country_canada').click()

start_date = browser.find_element_by_id('address_birthday')
type1 = 'string'
date2 = '15/11/2019'
browser.execute_script('arguments[0].setAttribute("type", "%s")' % type1, start_date)
browser.execute_script('arguments[0].setAttribute("value", "%s")' % date2, start_date)

browser.find_element_by_id('address_age').send_keys('23')
browser.find_element_by_id('address_picture').send_keys('/Users/alexmarcelo/Downloads/thermometer.png')
browser.find_element_by_id('address_website').send_keys('https://www.google.com')
browser.find_element_by_id('address_phone').send_keys('5529104857')
browser.find_element_by_id('address_interest_dance').click()
browser.find_element_by_id('address_note').send_keys('Soy una nota')

browser.find_element_by_name('commit').click()

#browser.close()
