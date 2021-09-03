import re
with open('./column_list.txt', encoding='utf-8') as read_f:
    cnt = 0
    append_line = str()
    for line in read_f:
        split_line = re.split('[\-\:\#\n]',line)
        if cnt <= 0:
            append_line = 'CREATE TABLE ' +split_line[1] +'(\n'
            cnt += 1
        else :
            append_line = append_line + split_line[1] + ' TEXT,\n'

    append_line = append_line + 'id INTEGER,\n PRIMARY KEY(id)\n)'
    with open('./create_table.sql','w') as write_f:
        write_f.write(append_line)



