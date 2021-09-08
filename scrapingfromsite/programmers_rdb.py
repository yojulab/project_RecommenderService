#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import sqlite3
import datetime
import schedule
from selenium import webdriver
from bs4 import BeautifulSoup


# In[2]:


browser = webdriver.Chrome('../../chromedriver.exe')


# In[3]:


def scrapping_site():
    uri = 'https://programmers.co.kr'
    url = 'https://programmers.co.kr/job?page=1&min_salary=&min_career=&min_employees=&order=recent'

    conn = sqlite3.connect('../db.sqlite3')
    c = conn.cursor()
    # c.execute("CREATE TABLE IF NOT EXISTS SCRAPPING_SITE "
    #           "(id INTEGER PRIMARY KEY AUTOINCREMENT, target_name TEXT, target_url TEXT, detail_target_url TEXT, "
    #           "category_big TEXT, category_middle TEXT , category_small TEXT, search_word TEXT, create_date TEXT, "
    #           "recruit_title TEXT, company_name TEXT, detail_uri TEXT, task TEXT, employment_type TEXT, "
    #           "company_info TEXT, need_career TEXT, salary TEXT, apply_start_date TEXT, apply_end_date TEXT, "
    #           "work_place TEXT, main_service TEXT, work_info TEXT, career_requirements TEXT, preference TEXT, "
    #           "company_culture TEXT, team_env TEXT)")

    browser.get(url)

    time.sleep(2)
    browser.implicitly_wait(2)

    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')

    length = soup.select('h5.position-title')
    leng = len(length)

    for j in range(leng):
        job = ''
        work = ''
        career = ''
        money = ''
        company = ''
        service = ''
        period = ''
        position = ''
        nowDate = ''
        category_middle = ''
        category_small = ''
        search_word = ''
        html = ''
        soup = ''

        time.sleep(2)
        browser.implicitly_wait(2)

        html = browser.page_source
        soup = BeautifulSoup(html, 'html.parser')

        sel = soup.select('h5 > a[href]')[j]
        href = sel['href']

        detail_uri = uri+href

        browser.get(detail_uri)
        time.sleep(2)
        browser.implicitly_wait(2)
        html = browser.page_source
        soup = BeautifulSoup(html,'html.parser')

        recruit_title = soup.select('h2.title')[0].text.strip()
        company_name = soup.select('h4.sub-title')[0].text.strip()

        summary = soup.select('table.table-information > tbody > tr > td.t-label')
        summval = soup.select('table.table-information > tbody > tr > td.t-content')
        summlen = len(summary)

        for k in range(summlen):
            if summary[k].text.strip() == '직무':
                job = summval[k].text.strip()
            elif summary[k].text.strip() == '고용 형태':
                work = summval[k].text.strip()
            elif summary[k].text.strip() == '경력':
                career = summval[k].text.strip()
            elif summary[k].text.strip() == '연봉':
                money = summval[k].text.strip()
            elif summary[k].text.strip() == '회사 규모':
                company = summval[k].text.strip()
            elif summary[k].text.strip() == '주요 서비스':
                service = summval[k].text.strip()
            elif summary[k].text.strip() == '기간':
                period = summval[k].text.strip()
            elif summary[k].text.strip() == '근무 위치':
                position = summval[k].text.strip()


        if period == '상시 채용':
            start_date = ''
            end_date = '20211231'
        else:
            start_date = period[0:16].replace(' ','').replace('-','').replace(':','')
            end_date = period[20:36].replace(' ','').replace('-','').replace(':','')

        try:
            intro = soup.select('div#job-position-description-view-section > div')
            intro = intro[0].text.strip().replace('\n', '')
        except:
            intro = ''

        try:
            cond = soup.select('div#job-position-requirement-view-section > div')
            cond = cond[0].text.strip().replace('\n', '')
        except:
            cond = ''

        try:
            prefe = soup.select('div#job-position-preferredExperience-view-section > div')
            prefe = prefe[0].text.strip().replace('\n', '')
        except:
            prefe = ''

        try:
            table = soup.select('table.table-dev-culture')
            table = table[0].text.strip().replace('\n', '')
        except:
            table = ''

        try:
            culture = soup.select('div#job-position-additionalInformation-view-section > div')
            culture = culture[0].text.strip().replace('\n', '')
        except:
            culture = ''

        now = datetime.datetime.now()
        nowDate = now.strftime('%Y%m%d')

    #     print('프로그래머스', uri, url, 'IT', category_middle, category_small, search_word, nowDate, recruit_title, company_name, detail_uri, job, work, company, career, money, start_date, end_date, position, service, intro, cond, prefe, culture, table)
        c.execute("INSERT INTO SCRAPPING_SITE"
                  "(target_name, target_url, detail_target_url, category_big, category_middle, category_small, "
                  "search_word , create_date, recruit_title, company_name, detail_uri, task, employment_type, "
                  "company_info, need_career, salary, apply_start_date, apply_end_date, work_place, main_service, "
                  "work_info, career_requirements, preference, company_culture, team_env) "
                  "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                  ('프로그래머스', uri, url, 'IT', category_middle, category_small,
                   search_word, nowDate, recruit_title, company_name, detail_uri, job, work,
                   company, career, money, start_date, end_date, position, service,
                   intro, cond, prefe, culture, table))

        browser.back()

    conn.commit()
    c.close()

scrapping_site()



