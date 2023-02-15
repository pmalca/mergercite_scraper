from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time 
from bs4 import BeautifulSoup
import requests
import csv
from tqdm import tqdm
import pandas as pd

def scrape_merger_cases(path_1:str,url:str)->None:

    n_cases =[]
    cases_name =[]
    links = []
    not_dates =[]
    dec_dates = []
    decisions = []
    phase = []
    sectors = []
    language = []

    driver = webdriver.Chrome(path_1)
    driver.get(url)

    driver.find_element(By.ID, 'button').click()

    time.sleep(10)

    repeat_count = 164

    for i in range(repeat_count):

        html = driver.page_source
        soup = BeautifulSoup(html, "lxml")
        print(len(soup.find_all("table")))
        
        table_1 = soup.find("table", {"id": "DataTables_Table_0"})

        for row in tqdm(table_1.findAll('tr')[1:]):
            n_case = row.findAll('td')[0].text
            case_name = row.findAll('td')[1].text
            not_date = row.findAll('td')[2].text
            dec_date = row.findAll('td')[3].text
            decision = row.findAll('td')[4].text
            phas = row.findAll('td')[5].text
            sector = row.findAll('td')[6].text
            lang = row.findAll('td')[7].text
            link = row.a['href']

            n_cases.append(n_case)
            cases_name.append(case_name)
            not_dates.append(not_date)
            dec_dates.append(dec_date)
            decisions.append(decision)
            phase.append(phas)
            sectors.append(sector)
            language.append (lang)
            links.append(link)

        driver.find_element(By.ID, 'DataTables_Table_0_next').click()
        
        time.sleep(10)
        
    df = pd.DataFrame(list(zip(n_cases, cases_name, not_dates, dec_dates, decisions, phase, sectors, language, links)), 
                    columns =['Case', "Case Name", 'Notification Date', 'Decision Date', 'Decision', 'Phase', "Sector", "Language", "Link"])
    df = df.reset_index(drop=True)

    df.to_csv('path_save/merger_cases.csv', index=False)


path_1 = "driver_path"
url = "https://apps.mergercite.eu/shiny/mergercite/"

scrape_merger_cases(path_1, url)
