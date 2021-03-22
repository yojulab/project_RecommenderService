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
    sumary_value = list()
    for summary in summaries:
        summary = summary.find_all(name='td', attrs={'class': ['t-label','t-content']})
        label = summary[0].text.strip()
        if label in sumary_list:
            index = sumary_list.index(label)
            sumary_value.insert(index, summary[1].text)    # 직무	프론트엔드

    tech_stacks = soup_detial.select(selector='div.content-body>.section-stacks>table>tbody>tr>td>code')
    t01 = list()
    for tech_stack in tech_stacks:
        t01.append(tech_stack.string)

    print(company_name, detail_url, sumary_value[0], t01)
    # tech_stacks = soup_detial.select(selector='div.content-body>.section-stacks>table>tbody>tr>td>code')


