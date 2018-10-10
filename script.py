"""
<   This code script.py is to be used for learning purposes only and should not be
    used a tool for any commercial purpose.

    All rights reserved ® 2018  David Craven

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""

import csv
import parameters
from parsel import Selector
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# function to ensure all key data fields have a value
def validate_field(field):
    # if field is present pass if field:
    if field:
        pass
    # if field is not present print text else:
    else:
        field = 'No results'
    return field


# defining new  variable passing two parameters
writer = csv.writer(open(parameters.file_name, 'wb'))

# writerow() method to the write to the file object
writer.writerow(['Name', 'Job Title', 'Company', 'College', 'Location', 'URL'])

# specifies the path to the chromedriver.exe
driver = webdriver.Chrome('/Users/davidcraven/Downloads/chromedriver')

# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.linkedin.com')

# locate email form by_class_name
username = driver.find_element_by_class_name('login-email')

# send_keys() to simulate key strokes
username.send_keys(parameters.linkedin_username)

# sleep for 0.5 seconds
sleep(0.5)

# locate password form by_class_name
password = driver.find_element_by_class_name('login-password')

# send_keys() to simulate key strokes
password.send_keys(parameters.linkedin_password)
sleep(0.5)

# locate submit button by_xpath
sign_in_button = driver.find_element_by_xpath('//*[@type="submit"]')

# .click() to mimic button click
sign_in_button.click()
sleep(0.5)

# driver.get method() will navigate to a page given by the URL address
driver.get('https:www.google.com')
sleep(3)

# locate search form by_name
search_query = driver.find_element_by_name('q')

# send_keys() to simulate the search text key strokes
search_query.send_keys(parameters.search_query)
sleep(0.5)

# navigate to the URL address specified by search_query in parameters.py
driver.get(parameters.search_query)

# .send_keys() to simulate the return key
search_query.send_keys(Keys.RETURN)
sleep(3)

# locate URL by_class_name
linkedin_urls = driver.find_elements_by_class_name('iUh30')

# variable linkedin_url is equal to the list comprehension
linkedin_urls = [url.text for url in linkedin_urls]
sleep(0.5)

# For loop to iterate over each URL in the list returned from the google search query
for linkedin_url in linkedin_urls:

    # get the profile URL
    driver.get(linkedin_url)
    sleep(5)

    # assigning the source code for the web page to variable sel
    sel = Selector(text=driver.page_source)

    # xpath to extract the text from the class containing the name
    name = sel.xpath('//*[starts-with(@class, "pv-top-card-section__name")]/text()').extract_first()

    # if name exists
    if name:
        # .strip() will remove the new line /n and white spaces
        name = name.strip()

    # xpath to extract the text from the class containing the job title
    job_title = sel.xpath('//*[starts-with(@class, "pv-top-card-section__headline")]/text()').extract_first()

    if job_title:
        job_title = job_title.strip()

    # xpath to extract the text from the class containing the company
    company = sel.xpath('//*[starts-with(@class, "pv-top-card-v2-section__entity-name pv-top-card-v2-section__company-name")]/text()').extract_first()

    if company:
        company = company.strip()

    # xpath to extract the text from the class containing the college
    college = sel.xpath('//*[starts-with(@class, "pv-top-card-v2-section__entity-name pv-top-card-v2-section__school-name")]/text()').extract_first()

    if college:
        college = college.strip()

    # xpath to extract the text from the class containing the location
    location = sel.xpath('//*[starts-with(@class, "pv-top-card-section__location")]/text()').extract_first()

    if location:
        location = location.strip()

    # assignment of the current URL
    linkedin_url = driver.current_url

    # validating if the fields exist on the profile
    name = validate_field(name)
    job_title = validate_field(job_title)
    company = validate_field(company)
    college = validate_field(college)
    location = validate_field(location)
    linkedin_url = validate_field(linkedin_url)

    # printing the output to the terminal
    print('\n')
    print('Name: ' + name)
    print('Job Title: ' + job_title)
    print('Company: ' + company)
    print('College: ' + college)
    print('Location: ' + location)
    print('URL: ' + linkedin_url)
    print('\n')

    # writing the corresponding values to the header
    # encoding with utf-8 to ensure all characters get loaded
    writer.writerow([name.encode('utf-8'),
                     job_title.encode('utf-8'),
                     company.encode('utf-8'),
                     college.encode('utf-8'),
                     location.encode('utf-8'),
                     linkedin_url.encode('utf-8')])

# terminates the application
driver.quit()
