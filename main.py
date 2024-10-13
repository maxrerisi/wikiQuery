from parsehtml import func
import wikipedia

srch = input("search query? > ")
# Search for a topic
search_results = wikipedia.search(srch)
for a, b in enumerate(search_results):
    print(a, b)

print()
selection = int(input("select which one you want > "))
srch = search_results[selection]
print(srch)
# print(f"Search Results: {search_results}")
# print("-"*150)

# Get a summary of a Wikipedia page
# summary = wikipedia.summary(srch, sentences=2)
# print(f"Summary: {summary}")

# Fetch the full page content
page = wikipedia.page(srch, auto_suggest=False)
print(f"Title: {page.title}")
print(f"URL: {page.url}")
with open('out.txt', 'w') as fp:
    # print("Content: ", page.content)
    fp.write(page.content)

with open('htmlout.html', 'w') as fp:
    fp.write(page.html())

# <table class="infobox ib-company vcard"> is the class of the table we want

func() 