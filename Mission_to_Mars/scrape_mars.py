from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from pprint import pprint

def scrape():
    browser = Browser('chrome', executable_path=ChromeDriverManager().install(), headless=True)

    url = 'https://redplanetscience.com/'
    browser.visit(url)

    html = browser.html
    # print(html)

    soup = BeautifulSoup(html, 'html.parser')

    dates = soup.find('div', class_='list_date').text
    news_titles = soup.find('div', class_='content_title').text
    news_article = soup.find('div', class_='article_teaser_body').text

    # pprint(dates)
    # pprint(news_titles)
    # pprint(news_article)

    Spaceurl = 'https://spaceimages-mars.com'
    browser.visit(Spaceurl)
    browser.find_by_tag("button")[1].click()

    html = browser.html
    # print(html)

    soup = BeautifulSoup(html, 'html.parser')

    featured_image = soup.find('img', class_='fancybox-image')
    featured_image_source = soup.find('img', class_='fancybox-image').get("src")
    image_source = "https://spaceimages-mars.com/" + featured_image_source

    # pprint(featured_image)
    # pprint(featured_image_source)
    # pprint(image_source)


    marsfacturl = 'https://galaxyfacts-mars.com'

    tables = pd.read_html(marsfacturl)
    # tables

    df = tables[0]
    df1 = df.iloc[0]
    df1.head().to_list()
    df.columns = df1.head().to_list()
    df2 = df.set_index("Mars - Earth Comparison")
    df2 = df2.drop(index ='Mars - Earth Comparison')
    df2.index.name = 'Description'
    # df2.head()

    html_table = df.to_html()
    # html_table

    Astrourl = 'https://marshemispheres.com/'
    browser.visit(Astrourl)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    hemispheres_hyperlinks = browser.find_by_css("a.product-item img")
    len(hemispheres_hyperlinks)

    images_list = []
    #images_dict= {}
    for img in range(len(hemispheres_hyperlinks)):    
        browser.find_by_css("a.product-item img")[img].click()
        sample_button = browser.find_by_text("Sample")
        href = sample_button['href']
        #image_urls.append(href)
        hemisphere_name = browser.find_by_tag("h2")
        title = hemisphere_name.value
        images_dict = {"title":title, "img_url":href}
        images_list.append(images_dict)
        #button = sample_button.outer_html
        #buttons.append(button)
        #print(sample_button.outer_html)
        #print(browser.find_by_text("Sample"))
        browser.visit(Astrourl)



    Mars_data = {
        "news_title": news_titles,
        "news_article": news_article,
        "featured_image": image_source,
        "html_table": html_table,
        "image_urls": images_list
        }
    return Mars_data
