import requests
from bs4 import BeautifulSoup

url_main = 'https://www.saramin.co.kr/zf_user/jobs/list/job-category'
url_param = '?cat_bcd=4'
res = requests.get(url_main+url_param)

# res.status_code, res.content
soup = BeautifulSoup(res.content, 'lxml')
groups = soup.find_all(name=['li', 'div'], attrs={'class': ['item','lookup', 'effect_bold', 'list_item']})

surfix_url = 'https://www.saramin.co.kr'
total_count = 0
print('total groups : ', len(groups))
data = list()

for group in groups:
    divide = group['class'][0].strip()
    if divide == 'item':        # 그랜드 상품
        detail_url = surfix_url + group.a['href']       # 상세 링크
        company_name = group.a.contents[3].string       # 회사명
        recruit_title = group.strong.string             # 모집 주제
        apply_end_date = group.contents[5].string       # 마감일
        need_career = group.ul.contents[1].string       # 경력
        need_education = group.ul.contents[3].string    # 학력
        employment_type = ''    # 채용 종류
        work_place = group.ul.contents[5].string        # 근무지역
        total_count += 1

    elif divide in ['lookup', 'effect_bold'] :      # 프리미엄, 포커스 상품
        detail_url = surfix_url + group.a['href']       # 상세 링크
        company_name = group.h3.string                  # 회사명
        recruit_title = group.h4.string                 # 모집 주제
        apply_end_date = group.contents[5].span.string  # 마감일
        need_career = group.ul.li.string       # 경력
        need_education = group.ul.contents[3].string    # 학력
        employment_type = ''    # 채용 종류
        work_place = group.ul.contents[5].string        # 근무지역
        total_count += 1

    elif divide == 'list_item' :        # 전체 채용 정보
        detail_url = surfix_url + group.a['href']       # 상세 링크
        company_name = group.contents[3].span.string    # 회사명
        recruit_title = group.contents[5].a.span.string                 # 모집 주제
        apply_end_date = group.contents[11].contents[3].contents[0]  # 마감일
        need_career = group.contents[7].p.string       # 경력
        need_education = group.contents[7].contents[1].string    # 학력
        employment_type = group.contents[9].p.string    # 채용 종류
        work_place = group.contents[9].contents[1].string        # 근무지역
        total_count += 1

    # compare to DB
    info = dict()
    info['detail_url'] = detail_url       # 상세 링크
    info['company_name'] = company_name   # 회사명
    info['recruit_title'] = recruit_title             # 모집 주제
    info['create_date'] = ''                 # 등록일 (`21.03.04)
    info['apply_end_date'] = apply_end_date       # 마감일
    info['need_career'] = need_career      # 경력
    info['need_education'] = need_education    # 학력
    info['employment_type'] = employment_type    # 채용 종류
    info['work_place'] = work_place        # 근무지역
    print(info)

    data.append(info)


# 회원님과 높은 확률로 매칭된 추천공고
# groups = soup.select(selector='div.list_row>.col')
# print('total groups : ', len(groups))
# for group in groups:
# 
#     # compare to DB

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
