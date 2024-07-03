import datetime

date_of_birth = datetime.datetime(1981, 1, 1)
male = True

day_counter = 0
if male: 
    day_counter = 1
if not male:
    day_counter = 2

for i in range(100):
    rr_num = ""
    year = str(date_of_birth.year)[-2:]
    month = str(date_of_birth.month).zfill(2)
    day = str(date_of_birth.day).zfill(2)
    counter = str(day_counter).zfill(3)
    rr_num = f"{year}{month}{day}{counter}"

    check = str(97 - (int(rr_num) % 97)).zfill(2)
    rr_num = rr_num + check

    print(rr_num)

    day_counter = day_counter + 2