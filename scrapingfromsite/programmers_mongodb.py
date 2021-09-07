import requests
from bs4 import BeautifulSoup

url_main = 'https://programmers.co.kr/job'
url_param = ''
res = requests.get(url_main+url_param)

# res.status_code, res.content
soup = BeautifulSoup(res.content, 'lxml')
groups = soup.select(selector='.list-position-item')						# list type

total_count = 0
surfix_url = 'https://programmers.co.kr/'
data = list()
for group in groups:
    info = dict()
    detail_url = surfix_url + group.h5.a['href']
    info['detail_url']  = detail_url
    info['company_name'] = group.h6.find(text=True, recursive=False).strip()    # or group.h6.contents[0].strip()
    info['recruit_title'] = group.h5.a.string             # 모집 주제

    # compare to DB

    # detial 
    res_detail = requests.get(detail_url)
    soup_detail = BeautifulSoup(res_detail.content, 'lxml')
    summaries = soup_detail.select(selector='section.section-summary>table>tbody>tr')
    summary_list = ['직무', '고용 형태', '경력', '연봉', '회사 규모', '주요 서비스', '기간', '위치']
    summary_info = ['task','employment_type','need_career','salary','company_info','main_service','apply_end_date','work_place']

    summary_value = list()
    for summary in summaries:
        label = summary.contents[3].string.strip()
        if label in summary_list:
            index = summary_list.index(label)
            info[summary_info[index]] = summary.contents[5].string

    tech_stacks = soup_detail.select(selector='div.content-body>.section-stacks>table>tbody>tr>td>code')
    hash_tag = list()
    for tech_stack in tech_stacks:
        hash_tag.append(tech_stack.string)
    info['hash_tag'] = hash_tag
    total_count += 1

    data.append(info)

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
