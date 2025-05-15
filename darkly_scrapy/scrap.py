#!/usr/bin/env python3 import requests
import bs4 as bs

def scrapping_recursive(url):
	r = requests.get(url)
	s = bs.BeautifulSoup(r.text, html.parser)
	if (s is not None):
		links = s.find_all("a")
		f = open("results.txt", "a+")
		for link in links:
			final_link = link.get(href)
			if (final_link == "README"):
				r = requests.get(url + final_link)
				if "Demande" not in r.text and "Toujours" not in r.text:
					if "Tu" not in r.text and "Non" not in r.text:
						f.write(r.text)
			elif (final_link != "../"):
				scrapping_recursive(url + final_link)
		f.close()

url = "http://localhost:8080/.hidden/"
scrapping_recursive(url)
