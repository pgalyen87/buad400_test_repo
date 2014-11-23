from bs4 import BeautifulSoup
import requests

output_dir = 'data'

base_url = "http://www.nydailynews.com/blogs/dailypolitics"

n = 5

soup = BeautifulSoup(requests.get(base_url).text)
#print soup.prettify().encode('ascii', 'ignore')

# writes content 'text' to a file in specified directory with filename 'title'.txt
def write_page(dir, title, text):
	wfile = open(dir+ "/" + title + '.txt', 'w')
	wfile.write(text)
	wfile.close()
	
#write_page("data", 'test', "abcdef")


articles = soup.find_all('article')
#print articles

visited = 0
i = 0


while(visited < min(n, len(articles)) and i < len(articles)):
	try:
		# Do something
		link = articles[i].a.get('href')
		print('Scraping: ' + link)
		curr_soup = BeautifulSoup(requests.get(link).text)
		
	except: 
		print "UNABLE TO SCRAPE!"
		
	i += 1	