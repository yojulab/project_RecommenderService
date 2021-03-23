import requests
from bs4 import BeautifulSoup

url_main = 'https://www.saramin.co.kr/zf_user/jobs/list/job-category'
url_param = '?cat_bcd=4'
res = requests.get(url_main+url_param)

# res.status_code, res.content
soup = BeautifulSoup(res.content, 'lxml')
groups = soup.select(selector='ul.list_product>li.item')						# list 그랜드 type

surfix_url = 'https://www.saramin.co.kr'
for group in groups:
    # print(group)
    detail_url = surfix_url + group.a['href']
    company_name = group.a.contents[3].string    # or group.h6.contents[0].strip()
    apply_end_date = group.contents[5].string

    # compare to DB

    # detial 
    res_detial = requests.get(detail_url)
    soup_detial = BeautifulSoup(res_detial.content, 'lxml')
    items_detial = soup_detial.select(selector='div.jview')
    
    summaries = items_detial[0].select(selector='.jv_summary>div.cont>div.col')
    
    sumary_list = ['경력', '학력', '근무형태', '우대사항', '급여', '직급/직책', '근무일시', '근무지역']
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


