import re
from datetime import datetime, timedelta

def get_apply_end_date(apply_end_date):     # string to yyyymmdd
    now = datetime.now()  # current date and time
    current_year = now.strftime("%Y")
    result = apply_end_date
    if result:      # in case param is not NULL
        withoutkorean = re.search("[^ㄱ-힣]+", apply_end_date)
        if withoutkorean:   # in case without any charactors
            withD = re.search("[D-]", apply_end_date)
            days = re.split("[^\d]+", apply_end_date)
            if withD:   # with day D
                d_day = now + timedelta(int(days[1]))
                result = d_day.strftime("%Y%m%d")
            elif len(days) > 1:       # mm/dd
                result = current_year + days[1].zfill(2) + days[2].zfill(2)
            else:       # yyyymmdd
                result = days[0]
        else:
            if apply_end_date == '오늘마감':
                result = now.strftime("%Y%m%d")
            else :  # 상시채용 등
                result = current_year+'1230'

    return result   # yyyymmdd type