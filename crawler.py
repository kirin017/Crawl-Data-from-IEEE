from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


def crawl_author_articles(author_name):
    # Khởi tạo trình điều khiển cho trình duyệt Chrome
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options = options, executable_path="chromedriver.exe")
    # Truy cập vào web IEEE
    driver.get('https://ieeexplore.ieee.org/Xplore/home.jsp')

    # Điền thông tin tác giả
    search_box = driver.find_element(by=By.XPATH, value = '//*[@id="LayoutWrapper"]/div/div/div[3]/div/xpl-root/header/xpl-header/div/div[2]/div[2]/xpl-search-bar-migr/div/form/div[2]/div/div[1]/xpl-typeahead-migr/div/input')
    search_box.send_keys(author_name)

    # Nhấn nút tìm kiếm
    search_button = driver.find_element(by=By.XPATH, value = '//*[@id="LayoutWrapper"]/div/div/div[3]/div/xpl-root/header/xpl-header/div/div[2]/div[2]/xpl-search-bar-migr/div/form/div[2]/div/div[2]')
    search_button.click()

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    papers = soup.find_all('div',class_="col result-item-align px-3")
    
    for paper in papers:
        title = soup.find('h3',class_="result-item-title").text
        authors = soup.find('p', "author text-base-md-lh").text
        publisher_info = soup.find('div', 'description').find('a').text
        publisher = soup.find('div', "description").find('div', "publisher-info-container").text
        print("Title:", title)
        print("Author", authors)
        print("Description: ", publisher_info)
        print("Publisher: ", publisher)
    driver.quit()
    return 0
    
    # Đóng trình điều khiển
author_name = input()
crawl_author_articles(author_name)
