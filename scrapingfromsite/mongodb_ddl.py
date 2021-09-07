from pymongo import MongoClient
db_address = 'mongodb://127.0.0.1:27017/'

client = MongoClient(db_address)  # with Docker inspect
mydb = client.db_scraping						# get Database

data = {'title': 'mariaDB 보기', 'tags': ['디비 서비스']}

data = {'apply_end_date': '', 'company_name': '국내 대기업 계열 건설사', 'create_date': '(`21.01.15)', 'detail_url': 'https://www.jobindex...view/41031', 'employment_type': '', 'hash_tag': ['#비주거개발사업', '#비주거사업지원', '#기획설계', '#복합시설공모', '#복합시설설계'], 'need_career': '', 'need_education': '', 'recruit_title': '사업지원 담당자 (대리 ~ 차장급)', 'work_place': ''}

board_info = mydb.periodicity_scraping.insert_one(data)

data = [{"name": "Ram", "age": "26", "city": "Hyderabad"},
        {"name": "Rahim", "age": "27", "city": "Bangalore"}]

data = [{'detail_url': 'https://www.jobindexworld.com/jobpost/view/41031', 'company_name': '국내 대기업 계열 건설사', 'recruit_title': '사업지원 담당자 (대리 ~ 차장급)', 'create_date': '(`21.01.15)', 'apply_end_date': '', 'need_career': '', 'need_education': '', 'employment_type': '', 'work_place': '', 'hash_tag': ['#비주거개발사업', '#비주거사업지원', '#기획설계', '#복합시설공모', '#복합시설설계']}, {'detail_url': 'https://www.jobindexworld.com/jobpost/view/41012', 'company_name': '국내 대기업 계열 건설사', 'recruit_title': '주택 사업 담당자 (대리 ~ 차장급)', 'create_date': '(`21.01.14)', 'apply_end_date': '', 'need_career': '', 'need_education': '', 'employment_type': '', 'work_place': '', 'hash_tag': ['#주택사업', '#임대아파트사업', '#부동산개발', '#부동산사업기획', '#부동산사업분석']}]


res = mydb.periodicity_scraping.insert_many(data)
print(res.inserted_ids)

board_info = mydb.periodicity_scraping.find()			# get Collection with find()
for info in board_info:						# Cursor
    print(info)
