from selenium import webdriver
import pandas as pd
from tqdm import tqdm

def crawling(rangelen, startnum, savename):
    driver = webdriver.Chrome(executable_path='/Users/kimgyuri/Desktop/chromedriver')
    df = pd.DataFrame(columns=['URL', 'Title', 'User'])
    for num in tqdm(range(rangelen)): #1000, 1000, 1000, 644
        num += startnum #1,1001,2001,3001,4001
        print(num)
        URL = 'https://www.10000recipe.com/recipe/list.html?order=reco&page=' + str(num)
        driver.get(url=URL)

        elements = driver.find_elements_by_xpath('//*[@id="contents_area_full"]/ul/ul/li')
        elements_len = len(elements)
        
        if elements_len == 0:
            break

        for i in range(elements_len):
            url_link = driver.find_elements_by_xpath('//*[@id="contents_area_full"]/ul/ul/li['+(str(i+1))+']/div[1]/a')
            url_link = url_link[0].get_attribute('href')
            title = driver.find_elements_by_xpath('//*[@id="contents_area_full"]/ul/ul/li['+(str(i+1))+']/div[2]/div[1]')
            title = title[0].text
            name = driver.find_elements_by_xpath('//*[@id="contents_area_full"]/ul/ul/li['+(str(i+1))+']/div[2]/div[2]')
            name= name[0].text
            df.loc[len(df)] = [url_link, title, name]
        df.to_csv(savename)
        
        
def main():
    crawling(1000,1,'10000recipe1.csv')
    crawling(1000,1001,'10000recipe2.csv')
    crawling(1000,2001,'10000recipe3.csv')
    crawling(1000,3001,'10000recipe4.csv')
    crawling(650,4001,'10000recipe5.csv')

if __name__ == "__main__":
    main()