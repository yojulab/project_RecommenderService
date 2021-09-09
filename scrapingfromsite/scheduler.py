import schedule
import time

import datetime
import sqlite3

import saramin_co_kr_rdb
import programmers_rdb

def job_site(target_site_name):
    print("I'm working...:", target_site_name)
    start_date = datetime.datetime.now()
    end_date = datetime.datetime.min
    during_time = datetime.datetime.min
    success = 'True'
    exception = str()
    total_count = 0
    try:
        if target_site_name == 'saramin':
            total_count = saramin_co_kr_rdb.scrapping_site()
        elif target_site_name == 'programmers':
            total_count = programmers_rdb.scrapping_site()
        else:
            pass

        end_date = datetime.datetime.now()
        during_time = end_date - start_date

    except Exception as e:
        success = 'False'
        exception = str(e)  # e.message : python2
        pass
    finally:
        print('total_count : ', total_count)
        connect = sqlite3.connect('../db.sqlite3')
        cursor = connect.cursor()
        cursor.execute("insert into do_scheduler(target_site_name, start_date, end_date, during_time, total_count,"
                       "success, exception) "
                       "values (?,?,?,?,?,?,?)",
                       (target_site_name, str(start_date), str(end_date), str(during_time), total_count,
                        success, exception))
        connect.commit()
        connect.close()


# schedule.every(1).minutes.do(job_site,'programmers')
# schedule.every(1).minutes.do(job_site,'saramin')
# schedule.every(2).hours.do(job_site,'programmers')
# schedule.every(2).hours.do(job_site,'saramin')
schedule.every(1).day.at("10:30").do(job_site,'saramin')
schedule.every(1).day.at("10:30").do(job_site,'programmers')
schedule.every(1).day.at("17:30").do(job_site,'saramin')
schedule.every(1).day.at("17:30").do(job_site,'programmers')

while True:
    schedule.run_pending()
    time.sleep(1)
