import requests
from bs4 import BeautifulSoup

def web_scrape(url, table_num):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    tables = soup.find_all("table", {"class": "wikitable"})
    table = tables[table_num]#index 1 table
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
        if row != [] and len(row) > 6:
            print(*row[:6])

if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/List_of_NBA_champions"
    print_column(get_data(url, 1))
    #print_data(get_data(url, 1))
