import bs4
import json
import wikipedia

# add functionality that stores last refresh and every month it recalculates
def get_queries(srch):
    with open('cache_search_keys.json', 'r') as fp:
        data = json.load(fp)
    srch = srch.lower()
    if srch in data:
        return data[srch]
    search_results = wikipedia.search(srch)
    data[srch] = search_results
    with open('cache_search_keys.json', 'w') as fp:
        json.dump(data, fp, indent=4)
    return search_results

def check_cache(qry, key):
    with open('cache_results.json', 'r') as fp:
        data = json.load(fp)

    if qry in data:
        if key in data[qry]:
            return data[qry][key]
    return None
    # print(data)


def update_cache(qry, key, res):
    with open('cache_results.json', 'r') as fp:
        data = json.load(fp)
    if qry not in data:
        data[qry] = {'query':qry}
    data[qry][key] = res
    with open('cache_results.json', 'w') as fp:
        json.dump(data, fp, indent=4)


def get_result(cleaned_query, search_key):
    out = check_cache(cleaned_query, search_key)
    if out:
        return out
    page = wikipedia.page(cleaned_query, auto_suggest=False)
    data = str(page.html())

    soup = bs4.BeautifulSoup(data, 'html.parser')
    tbl = bs4.BeautifulSoup(str(soup.findAll("table", class_="infobox ib-company vcard")), 'html.parser')
    # print(tbl)

    SEARCH = search_key # what you're looking for
    rows = tbl.find_all('tr')
    for row in rows:
        # Check if the search string exists in any of the row's text
        if SEARCH in row.get_text():
            # Get the individual cells (td elements) in the row
            cells = row.find_all('td')
            
            # Print the content of each cell,
            for cell in cells:
                out = cell.get_text()
                update_cache(cleaned_query, SEARCH, out)
                return out

            # TODO link should be some sort of different function bc it takes the text not actual url.
    return "Not Found."
