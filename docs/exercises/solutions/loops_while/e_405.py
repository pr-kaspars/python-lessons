page_number_sum = int(raw_input('Enter sum of page numbers: '))
sum = 0
page = 1
while sum < page_number_sum:
    sum += page
    page += 1
if sum is page_number_sum:
    print('Number of pages: ' + str(page))
else:
    print('Not possible')
