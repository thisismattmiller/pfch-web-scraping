import requests
from bs4 import BeautifulSoup
import json
import time

all_data = []
item_counter = 0

total_pages = range(0,950)

for page_number in total_pages:

	url = 'http://collection.mam.org/search.php?s='

	url = url + str(page_number)

	print("Working on... ",url)

	page_request_results = requests.get(url)

	page_html = page_request_results.text

	soup = BeautifulSoup(page_html, "html.parser")

	all_divs = soup.find_all("div", attrs = {'class':'object-work'})

	#looping though div (aka each artwork)
	for a_div in all_divs:

		all_li_el_in_div = a_div.find_all('li')
		creator_stmts_li = all_li_el_in_div[0:-1]
		creators = []
		for li_el in creator_stmts_li:
			creators.append(li_el.text)

		title_li = all_li_el_in_div[-1]

		a_link = title_li.find('a')

		title = a_link.text
		link = 'http://collection.mam.org/' + a_link['href']

		artwork = {
			"creators": creators,
			"title" : title,
			"url" : link
		}

		all_data.append(artwork)
		# print(title, link)
		# print(creator_stmts)
		# print('---')

	item_counter = item_counter + 10


	json.dump(all_data, open('artworks.json','w'), indent=2)

	time.sleep(1)












