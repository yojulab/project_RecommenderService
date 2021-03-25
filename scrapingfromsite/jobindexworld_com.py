from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.page_load_strategy = 'eager'

path = '../chromedriver_89.0.4389.23'
driver = webdriver.Chrome(executable_path=path, options=options)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


url_main = 'https://www.jobindexworld.com/jobpost/list'
url_param = ''
driver.get(url_main+url_param)

# search button
from selenium.webdriver.common.keys import Keys
search_element = "//input[@id='search-value']"
search_word = "개발"
driver.find_element(By.XPATH, search_element).send_keys(search_word + Keys.ENTER)
import time
time.sleep(5)

# calculate click count from item count(등록된 정보)
# count_element = driver.find_element(By.XPATH, "//div[@class='circle-aside-cnt-in']//span")
# item_count = count_element.get_attribute("span")
item_count = 60
click_count = (int) (item_count / 20) - 1     # 20 : item per a page 

# click button 'more view'
for seq in range(click_count):
    more_element = "//button[@class='btn-more']"
    driver.find_element(By.XPATH, more_element).click()
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, more_element))
        )
    except Exception as e:
        print(e)    
    finally:
        pass

from bs4 import BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'lxml')
groups = soup.select(selector='article.cpn-circle-conts-item')						# list type

surfix_url = 'https://www.jobindexworld.com'
total_count = 0
print('total groups : ', len(groups))
for group in groups:
    detail_url = surfix_url + group.a['href']       # 상세 링크
    company_name = group.a.div.contents[5].string   # 회사명
    recruit_title = group.strong.string             # 모집 주제
    create_date = group.span.string                 # 등록일 (`21.03.04)
    apply_end_date = ''       # 마감일
    need_career = ''      # 경력
    need_education = ''    # 학력
    employment_type = ''    # 채용 종류
    work_place = ''        # 근무지역

    hash_tag = list()
    for content in group.div.contents[3].contents:
        if 'a' in content:
            hash_tag.append(content.string)

    total_count += 1
    print(company_name, detail_url, hash_tag)

print('total : ', total_count)
driver.quit()
