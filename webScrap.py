import requests
import sqlalchemy
import pyodbc
#import jupyterlab
import sqlite3

from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup

connection = pyodbc.connect('')
cursor=connection.cursor()


url = 'https://www.ratemyprofessors.com/campusRatings.jsp?sid=1402'
options = Options()
options.binary_location = ""
driver = webdriver.Chrome(chrome_options = options, executable_path=r'')
driver.get(url)
button = driver.find_element_by_id('loadMore')
while button.is_displayed():
    button.click()
#button.quit() 
comments = driver.find_elements_by_xpath('')
comments_list = []
for p in range(len(comments)):
    #comments[p].find_elements_by_xpath('//p')
    comments_list.append(comments[p].text)
    cursor.execute(""" INSERT INTO test_1 (comments) VALUES (?)""", comments[p].text)

connection.commit()
print('complet.')


#soup = BeautifulSoup(driver.text, "html.parser")
#proftags = drive.findAll("td", {"class": "comments" })
#comments = drive.findAll("p")
#comments