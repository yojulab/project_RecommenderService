import schedule
import time

import datetime
import sqlite3

import saramin_co_kr_rdb

def job_site(target_site_name):
    print("I'm working...:", target_site_name)
    start_date = datetime.datetime.now()
    end_date = str()
    during_time = str()
    success = 'True'
    exception = str()
    try:
        if target_site_name == 'saramin':
            saramin_co_kr_rdb.scrapping_saramin()
        else:
            pass

        end_date = datetime.datetime.now()
        during_time = end_date - start_date

    except Exception as e:
        success = 'False'
        exception = e
        pass
    finally:
        connect = sqlite3.connect('../db.sqlite3')
        cursor = connect.cursor()
        cursor.execute("insert into do_scheduler(target_site_name, start_date, end_date, during_time, success, exception) "
                       "values (?,?,?,?,?,?)",
                       (target_site_name, str(start_date), str(end_date), str(during_time), success, exception))
        connect.commit()
        connect.close()


schedule.every(10).minutes.do(job_site,'saramin')
# schedule.every(4).day.at("10:30").do(job_site,'saramin')
# schedule.every().day.at("10:30").do(job)

while True:
    schedule.run_pending()
    # print("I'm working...: schedule")
    time.sleep(1)
