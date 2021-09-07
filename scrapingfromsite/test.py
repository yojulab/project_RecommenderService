import datetime
start_date = datetime.datetime.now()
end_date = datetime.datetime.min
during_time = datetime.datetime.min
success = 'True'

end_date = datetime.datetime.now()
during_time = end_date - start_date
print(during_time)