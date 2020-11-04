from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import csv

#Grab Url
url = 'https://www.marketindex.com.au/asx-listed-companies'

## Act Like A Website
req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})

## Turn HTML content to script
source = urlopen(req).read()

## Create Soup Object
soup = BeautifulSoup(source, 'lxml')

## Create CSV file
csv_file = open('companies.csv', 'w')

## Create A Writer Object to write to file
csv_writer = csv.writer(csv_file)

## Create Table Headings
csv_writer.writerow(["Rank", "Company Code", "Company Name", "Price", "Change", "Percent", "Market", "Year"])

## Create A List
data = []

##Find Table Tag with Id
table = soup.find('table', id="asx_sp_table")

## Find Table Body Within Table Tag
table_body = table.find('tbody')

## Find All The Row in the Table
rows = table_body.find_all('tr')

## Extracting Data from table
for row in rows:
	## Extract All Columns
    columns = row.find_all('td')
	## Remove Empty Spaces in Column Data
    columns = [element.text.strip() for element in columns]
    #Add Each row data to a list
    data.append([element for element in columns if element])

for row_data in data[0:2175]:
	rank = row_data[0]
	# print(rank)
	code = row_data[1]
	# print(code)
	name = row_data[2]
	# print(name)
	price = row_data[3]
	# print(price)
	change = row_data[4]
	# print(change)
	percent = row_data[5]
	# print(percent)
	market = row_data[6]
	# print(market)
	year = row_data[7]
	# print(year)

	csv_writer.writerow([rank, code, name, price, change, percent, market, year])
csv_file.close()
# print("Done")