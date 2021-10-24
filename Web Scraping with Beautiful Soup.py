from bs4 import BeautifulSoup as bsoup 
import requests
import xml
from xml import etree
from xml.etree import ElementTree

def remove_tags(text) :   # This function can remove html tags 

    return ''.join(xml.etree.ElementTree.fromstring(str(text)).itertext()) 

url = 'https://sampleonlistore.htmlsave.net' 

response = requests.get(url)    # sending http get request

if response.status_code==200 :   # check if request is success

    data = response.text    

    page_soup = bsoup(data, 'html.parser')  # putting retrieved html code to parser

    item_titles = page_soup.find_all("p",{"class":"item_title"}) # get <p> tag that has class name 'item_title'

    item_prices = page_soup.find_all("b",{"class":"price"})     # <b> tag that has class "price"

    item_shipping = page_soup.find_all("p",{"class":"ship_method"}) 

    item_rating = page_soup.find_all("p",{"class":"rating"})

    for x in range(len(item_titles)) :   # iterate through list
        print('[',x+1,']',end=' ')         # Adding number to show order of the items (x is 0-9) so added 1 to it 
        print(remove_tags(item_titles[x]))  # print content each detail without tags
        print(remove_tags(item_prices[x]))
        print(remove_tags(item_shipping[x]))
        print(remove_tags(item_rating[x]))
        print('\n')                            # added new line 

    input('\nExit >') # This is to stop window from closing when runned directly