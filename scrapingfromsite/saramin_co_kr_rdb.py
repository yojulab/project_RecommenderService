import requests
from bs4 import BeautifulSoup

url_main = 'https://www.saramin.co.kr/zf_user/jobs/list/job-category'
url_param = '?cat_bcd=4'
res = requests.get(url_main+url_param)

# res.status_code, res.content
soup = BeautifulSoup(res.content, 'lxml')
groups = soup.find_all(name=['li', 'div'], attrs={'class': ['item','lookup', 'effect_bold', 'list_item']})

target_name = '사람인'
surfix_url = 'https://www.saramin.co.kr'
total_count = 0
print('total groups : ', len(groups))
data = list()

import sqlite3
connect = sqlite3.connect('../db.sqlite3')
cursor = connect.cursor()
for group in groups:
    divide = group['class'][0].strip()
    if divide == 'item':        # 그랜드 상품
        detail_uri = surfix_url + group.a['href']       # 상세 링크
        company_name = group.a.contents[3].string       # 회사명
        recruit_title = group.strong.string             # 모집 주제
        apply_end_date = group.contents[5].string       # 마감일
        need_career = group.ul.contents[1].string       # 경력
        need_education = group.ul.contents[3].string    # 학력
        employment_type = ''    # 채용 종류
        work_place = group.ul.contents[5].string        # 근무지역
        total_count += 1

    elif divide in ['lookup', 'effect_bold'] :      # 프리미엄, 포커스 상품
        detail_uri = surfix_url + group.a['href']       # 상세 링크
        company_name = group.h3.string                  # 회사명
        recruit_title = group.h4.string                 # 모집 주제
        apply_end_date = group.contents[5].span.string  # 마감일
        need_career = group.ul.li.string       # 경력
        need_education = group.ul.contents[3].string    # 학력
        employment_type = ''    # 채용 종류
        work_place = group.ul.contents[5].string        # 근무지역
        total_count += 1

    elif divide == 'list_item' :        # 전체 채용 정보
        detail_uri = surfix_url + group.a['href']       # 상세 링크
        company_name = group.contents[3].span.string    # 회사명
        recruit_title = group.contents[3].span.string                 # 모집 주제
        apply_end_date = group.contents[11].contents[3].contents[0]  # 마감일
        need_career = group.contents[7].p.string       # 경력
        need_education = group.contents[7].contents[1].string    # 학력
        employment_type = group.contents[9].p.string    # 채용 종류
        work_place = group.contents[9].contents[1].string        # 근무지역
        total_count += 1

    # compare to DB
    cursor.execute(
        "insert into SCRAPPING_SITE("
        "target_name,target_url,detail_uri, company_name, recruit_title,create_date,apply_end_date,need_career,need_education,employment_type,work_place) "
        "values(?,?,?,?,?,datetime('now'),?,?,?,?,?)",
        (target_name,surfix_url,detail_uri, company_name, recruit_title,apply_end_date,need_career,need_education,employment_type,work_place))

connect.commit()
connect.close()
print('total : ', total_count)