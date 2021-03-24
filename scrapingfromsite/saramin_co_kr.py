import requests
from bs4 import BeautifulSoup

url_main = 'https://www.saramin.co.kr/zf_user/jobs/list/job-category'
url_param = '?cat_bcd=4'
res = requests.get(url_main+url_param)

# res.status_code, res.content
soup = BeautifulSoup(res.content, 'lxml')
groups = soup.find_all(name='li', attrs={'class': ['item','lookup', 'effect_bold']})

surfix_url = 'https://www.saramin.co.kr'

total_count = 0
print('total groups : ', len(groups))
for group in groups:
    divide = group['class'][0].strip()
    if divide == 'item':
        detail_url = surfix_url + group.a['href']       # 상세 링크
        company_name = group.a.contents[3].string       # 회사명
        recruit_title = group.strong.string             # 모집 주제
        apply_end_date = group.contents[5].string       # 마감일
        need_career = group.ul.contents[1].string       # 경력
        need_education = group.ul.contents[3].string    # 학력
        work_local = group.ul.contents[5].string        # 근무지역
        total_count += 1

    elif divide in ['lookup', 'effect_bold'] :
        detail_url = surfix_url + group.a['href']       # 상세 링크
        company_name = group.h3.string                  # 회사명
        recruit_title = group.h4.string                 # 모집 주제
        apply_end_date = group.contents[5].span.string  # 마감일
        need_career = group.ul.li.string       # 경력
        need_education = group.ul.contents[3].string    # 학력
        work_local = group.ul.contents[5].string        # 근무지역
        total_count += 1

    # compare to DB

    # detial 
    print(company_name, detail_url, apply_end_date)

print('total : ', total_count)