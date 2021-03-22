import requests
from bs4 import BeautifulSoup

url_main = 'https://programmers.co.kr/job'
url_param = ''
res = requests.get(url_main+url_param)

# res.status_code, res.content
soup = BeautifulSoup(res.content, 'lxml')
groups = soup.select(selector='.list-position-item')						# list type

surfix_url = 'https://programmers.co.kr/'
for group in groups:
    # print(group)
    detail_url = surfix_url + group.h5.a['href']
    company_name = group.h6.find(text=True, recursive=False).strip()    # or group.h6.contents[0].strip()

    # compare to DB

    # detial 
    res_detial = requests.get(detail_url)
    soup_detial = BeautifulSoup(res_detial.content, 'lxml')
    summaries = soup_detial.select(selector='section.section-summary>table>tbody>tr')
    sumary_list = ['직무', '고용 형태', '경력', '연봉', '회사 규모', '주요 서비스', '기간', '위치']
    for summary in summaries:
        summary = summary.find_all(name='td', attrs={'class': ['t-label','t-content']})
        
        if summary[0].text.strip() == '직무':
            s01 = summary[1].string    # 직무	프론트엔드
        if summary[0].text.strip() == '고용 형태':
            s02 = summary[1].string    # 고용 형태	정규직
        if summary[0].text.strip() == '경력':
            s03 = summary[1].string    # 경력	경력 무관
        if summary[0].text.strip() == '연봉':
            s04 = summary[1].string    # 연봉	3000 ~ 5000 만원
        if summary[0].text.strip() == '회사 규모':
            s05 = summary[1].string    # 회사 규모	16명
        if summary[0].text.strip() == '주요 서비스':
            s06 = summary[1].string    # 주요 서비스	CLICK AI
        if summary[0].text.strip() == '기간':
            s07 = summary[1].string    # 기간	2021-03-22 09:00 부터 2021-03-29 23:59 까지
        if summary[0].text.strip() == '위치':
            s08 = summary[1].string    # 위치

    tech_stacks = soup_detial.select(selector='div.content-body>.section-stacks>table>tbody>tr>td>code')
    t01 = list()
    for tech_stack in tech_stacks:
        t01.append(tech_stack.string)

    print(company_name, detail_url, t01)
    # tech_stacks = soup_detial.select(selector='div.content-body>.section-stacks>table>tbody>tr>td>code')


