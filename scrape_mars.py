from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
# Dependencies
import os
from bs4 import BeautifulSoup
import requests
import pymongo
import pandas as pd

def scrape_info():
    # Setup splinter
    executable_path={'executable_path':ChromeDriverManager().install()}
    browser =Browser('chrome',**executable_path, headless=False) 
    news_title, news_paragraph = mars_news(browser)
    data_dict = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "feature_image": feature_image(browser),
        "mars_tables": mars_facts(),
        "mars_hemispheres": mars_hemisphere(browser)
    }
    browser.quit()
    return data_dict

def mars_news(browser):
    url='https://redplanetscience.com/'
    browser.visit(url)
    html = browser.html
    #Parse HTML with Beautiful soup
    soup = BeautifulSoup(html, 'html.parser')
    #Collect the latest News Title and Paragraph Text
    news_title = soup.find_all('div',class_='content_title')[0].text
    news_p = soup.find_all('div',class_='article_teaser_body')[0].text

    return news_title, news_p

def feature_image(browser):
    url='https://spaceimages-mars.com/'
    browser.visit(url)
    # HTML object
    html = browser.html
    #Parse HTML with Beautiful soup
    soup = BeautifulSoup(html, 'html.parser')
    # Find the image url for the current Featured Mars Image and assign the url 
    link = soup.find('a', class_='showimg fancybox-thumbs')
    href= link['href']
    featured_image_url = url + href
    return featured_image_url 

def mars_facts():
    url = 'https://galaxyfacts-mars.com/'
    tables = pd.read_html(url)
    df = tables[0]
    df.columns = ['Description', 'Mars', 'Earth']
    df.set_index('Description', inplace=True)
    html_table = df.to_html()
    html_table = html_table.replace('class="dataframe"', 'class= "table table-striped"')
    return html_table.replace('\n', '')

def mars_hemisphere(browser):
    url='https://marshemispheres.com/'
    browser.visit(url)
    # Iterate through all pages
    links = []
    for x in range(0,4):

        # HTML object
        html = browser.html
        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html, 'html.parser')
        # Find the url for the current mars hemisphere and assign the url 
        description = soup.find_all('div', class_='description')[x]
        href = description.find('a', class_="itemLink product-item")['href']
        hemisphere_url = url + href
        #append it to a list 
        links.append(hemisphere_url)
    hemisphere_image_urls = []
    for link in links:
        try:
            browser.visit(f'{link}')
            # HTML object
            html = browser.html
            # Parse HTML with Beautiful Soup
            soup = BeautifulSoup(html, 'html.parser')
            # Find the Hemisphere title containing the hemisphere name
            title = soup.find('h2', class_='title').text
            href = soup.find('div', class_= 'downloads').a['href']
            img_url = url + href 

            # Dictionary 
            Hem = {
                'title': title,
                'img_url': img_url,
            } 
            hemisphere_image_urls.append(Hem)
        except:
            print("Scraping Complete")
    return hemisphere_image_urls
        
    
