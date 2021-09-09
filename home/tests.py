from django.test import TestCase

# Create your tests here.
query = "select * from SCRAPPING_SITE where apply_end_date >= "+current_day+" and recruit_title like '"+search+"' order by apply_end_date"

cursor.execute("select * from SCRAPPING_SITE "
                       "where apply_end_date >= ?  and recruit_title like '"+search+"' "
                        "order by apply_end_date")

cursor.execute(query)
contact_list = cursor.fetchall()
len(contact_list)