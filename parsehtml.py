import bs4

def func():
    with open("htmlout.html", 'r') as fp:
        data = fp.read()

    soup = bs4.BeautifulSoup(data, 'html.parser')
    tbl = bs4.BeautifulSoup(str(soup.findAll("table", class_="infobox ib-company vcard")), 'html.parser')
    # print(tbl)

    srch = "Industry"
    rows = tbl.find_all('tr')
    for row in rows:
        # Check if the search string exists in any of the row's text
        if srch in row.get_text():
            # Get the individual cells (td elements) in the row
            cells = row.find_all('td')
            
            # Print the content of each cell,
            for cell in cells:
                out = cell.get_text()

    print(out)