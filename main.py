from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager


url = "https://www.dns-shop.ru/catalog/17a8a01d16404e77/smartfony"


# url = "https://www.dns-shop.ru/catalog/251c82c88ed24e77/smart-chasy-i-braslety/"

def run():
    serv = Service(ChromeDriverManager().install())
    opts = Options()
    opts.add_argument('start-maximized')
    #opts.add_argument('headless')
    driver = webdriver.Chrome(service=serv, options=opts)
    driver.get(url)
    try:
        WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div/div[3]/div[2]/a'))).click()
        sleep(1)
    except WebDriverException as e:
        print(e)
    try:
        elem = driver.find_elements(By.CLASS_NAME, "filters-extended__group")
        for tag_title in elem:
            print(tag_title.find_element(By.CLASS_NAME, 'filters-extended__group-title').text)
            filters = tag_title.find_elements(By.CLASS_NAME, 'filters-extended__filters-col')
            for fil in filters:
                span = fil.find_elements(By.CLASS_NAME, 'ui-collapse__link-text')
                for s in span:
                    print('\t' + s.text)
    except WebDriverException as e:
        print(e)
        print("Not found")
    finally:
        driver.quit()


if __name__ == '__main__':
    run()
