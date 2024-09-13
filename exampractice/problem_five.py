import datetime

# function1
def create_record():
    records = []
    while True:
        try:
            name, departure_date, country = input().split()
            # day, month, year = [int(i) for i in departure_date.split('/')]
            records.append([name, departure_date, country])
        except:
            break
    return records

# function2
# sort name by alphabet and departure_date_and_country by travel time
def sort_list(records: list):
    def sort_by_date(record):
        day, month, year = [int(i) for i in record[1].split('/')]
        return datetime.date(year, month, day)
    def sort_by_name(record):
        return record[0]
        
    return sorted(sorted(records, key=sort_by_date), key=sort_by_name)

# function3
def create_output(sorted_records):
    names, departure_dates_and_countries  = [], []

    # algorithmn for pseudo set
    for record in sorted_records:
        name = record[0]
        if name in names:
                continue
        else:
            names.append(name)
            departure_dates_and_countries.append([])

    for record in sorted_records:
        name, departure_date_and_country = record[0], f'{record[1]}:{record[2]}'
        idx = names.index(name)
        # append departure_date_and_country to specific departure_date_and_country array, and sort as well
        departure_dates_and_countries[idx].append(departure_date_and_country)
            
    # splat operator, like ... in js, in order to correctly format nested array
    return (names, *departure_dates_and_countries)
        
# input: sorted records
# return: (1) a list of user’s name and (2) a list of trip’s details with the
# index of each list corresponding to one another

# the main function
def main():
    records = create_record()
    sorted_records = sort_list(records)
    outputs = create_output(sorted_records)
    for idx, names in enumerate(outputs[0]):
        print(names, outputs[idx + 1])

main()

# call these three methods
# print out the sorted output in the correct format back to the user


# 
# Lisa ['25/1/2018:JP', '1/1/2023:TH']
# Pete ['2/2/2022:TW', '1/12/2022:JP']

# example input
# Pete 1/12/2022 JP
# Lisa 1/1/2023 TH
# Lisa 25/1/2018 JP
# Pete 2/2/2022 TW

# does both sort and create output, did this because didnt read instruction properly lol
# sort name by alphabet and departure_date_and_country by travel time
# def sort_and_create_output(records):
#     names, departure_dates_and_countries  = [], []
    
#     def sort_date(date):
#         day, month, year = [int(i) for i in date.split(':')[0].split('/')]
#         return datetime.date(year, month, day)
    
#     # algorithmn for pseudo set
#     for record in records:
#         name = record[0]
#         if name in names:
#                 continue
#         else:
#             names.append(name)
#             departure_dates_and_countries.append([])
#     names.sort()

#     for record in records:
#         name, departure_date_and_country = record[0], f'{record[1]}:{record[2]}'
#         idx = names.index(name)
        
#         # append departure_date_and_country to specific departure_date_and_country array, and sort as well
#         departure_dates_and_countries[idx] = sorted([*departure_dates_and_countries[idx], departure_date_and_country], key=sort_date)
            
#     # splat operator, like ... in js, in order to correctly format nested array
#     return (names, *departure_dates_and_countries)

