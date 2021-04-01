from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.page_load_strategy = 'eager'

path = '../chromedriver_89.0.4389.23'

try :

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
except:
    pass
finally :
    driver.quit()
    
groups = soup.select(selector='article.cpn-circle-conts-item')						# list type

surfix_url = 'https://www.jobindexworld.com'
total_count = 0
print('total groups : ', len(groups))
data = list()

for group in groups:
    info = dict()
    info['detail_url'] = surfix_url + group.a['href']       # 상세 링크
    info['company_name'] = group.a.div.contents[5].string   # 회사명
    info['recruit_title'] = group.strong.contents[0]             # 모집 주제
    info['create_date'] = group.span.string                 # 등록일 (`21.03.04)
    info['apply_end_date'] = ''       # 마감일
    info['need_career'] = ''      # 경력
    info['need_education'] = ''    # 학력
    info['employment_type'] = ''    # 채용 종류
    info['work_place'] = ''        # 근무지역

    hash_tag = list()
    for content in group.div.contents[3].contents:
        # something = re.findall("\<a", str(content))
        if '<a' in str(content):
            hash_tag.append(content.string)
    info['hash_tag'] = hash_tag
    total_count += 1
    print(info)

    data.append(info)

print('total : ', total_count)

# 프로젝트 root를 import 참조 경로에 추가
import os, sys
sys.path.append(os.getcwd())

from libraries import dml_mongodb
db_name = 'db_scraping'
collaction_name = 'periodicity_scraping'

try :
    insert_info = dml_mongodb.insert(db_name=db_name, collaction_name=collaction_name, data=data)
except:
    pass
finally :
    pass
