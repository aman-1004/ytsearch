from bs4 import BeautifulSoup as Soup
from selenium.webdriver import Chrome
import argparse

parser = argparse.ArgumentParser(description="Opens video on Youtube.")

parser.add_argument('-n',default=0, type=int, help='Index of video to open')
parser.add_argument('query',metavar="Query", type=str, help="Video Title")

args = parser.parse_args()
query = args.query
query = query.replace(" ",'+')
n = args.n

driver = Chrome()
driver.get(f"https://www.youtube.com/results?search_query={query}")

a_hrefs = driver.find_elements_by_id('video-title')
watchids = list(map(lambda x: x.get_attribute("href"), a_hrefs))


driver.get(watchids[n])

