import requests
from bs4 import BeautifulSoup
import wiki_script1 as wiki_script
#Same code from wiki_script1.py

def web_scrape(url, table_num):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    tables = soup.find_all("table", {"class": "wikitable"})
    table = tables[table_num]#index 0 table
    return table

def get_data(url, table_num):
    data = []
    table = web_scrape(url, table_num)
    rows = table.find_all("tr")
    for row in rows:
        row_data = []
        columns = row.find_all(["th", "td"])
        for column in columns:
                row_data.append(column.text.strip())
        data.append(row_data)

    return data

def print_data(data):
     for row in data:
        print(*row)

def print_column(data):
    for row in data:
        if row != []:
            print(*row[:1], *row[2:8])

if __name__ == '__main__':
    url = "https://en.wikipedia.org/wiki/List_of_Nobel_Memorial_Prize_laureates_in_Economic_Sciences"
    print_column(wiki_script.get_data(url, 0))
    #print_column(get_data(url, 0))
