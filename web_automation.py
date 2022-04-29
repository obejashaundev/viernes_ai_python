from lib2to3.pgen2 import driver
from re import X
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from viernes_say import *

driver = webdriver.Edge()

def whatDateIsIt():
    driver.get('https://www.bing.com/search?q=que%20fecha%20es')
    result = driver.find_element(By.XPATH, '//*[@id="b_results"]/li[1]/div[2]')
    date = result.text
    say('Hoy es '+date)

def whatTimeIsIt():
    driver.get('https://www.bing.com/search?q=que%20hora%20es')
    result = driver.find_element(By.XPATH, '//*[@id="digit_time"]')
    time = result.text
    say('Son las '+time)

def obtainWikipediaInfo(theme):
    driver.get(url="https://es.wikipedia.org/wiki/Wikipedia:Portada")
    input = driver.find_element_by_xpath(xpath='//*[@id="searchInput"]')
    input.click()
    input.send_keys(theme)
    
    submit = driver.find_element_by_xpath(xpath='//*[@id="searchButton"]')
    submit.click()
    
    resume = driver.find_element_by_xpath(xpath='//*[@id="mw-content-text"]/div[1]/p[2]')
    say(resume.text)

def playMusicVideo(titleVideo):
    driver.get(url="https://www.youtube.com/results?search_query="+titleVideo)
    video = driver.find_element_by_xpath(xpath='//*[@id="dismissible"]')
    video.click()
    
def translatePhraseBing(phrase):
    driver.get('https://www.bing.com/translator/?setlang=es')
    input = driver.find_element(By.XPATH, '//*[@id="tta_input_ta"]')
    input.send_keys(phrase)
    talk = driver.find_element(By.XPATH, '//*[@id="tta_output_ta"]')
    translate = talk.get_attribute('value')
    while ("..." in translate) or translate == "":
        translate = talk.get_attribute('value')
    print("Traducción: "+translate)
    say(translate)

def searchImages(description):
    driver.get('https://www.bing.com/search?q='+description)
    images = driver.find_element(By.XPATH, '//*[@id="b-scopeListItem-images"]/a')
    images.click()
    say('Estos son los resultados de búsqueda en imágenes sobre '+description)
    
#playMusicVideo('Un corazón')
#obtainWikipediaInfo('Linus Torvalds')
#translatePhraseBing("Buenas tardes")
#whatDateIsIt()
#whatTimeIsIt
#searchImages('Linus Torvalds')