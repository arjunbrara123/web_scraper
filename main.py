from selenium import webdriver

chrome_driver_path = 'chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

target_url = "https://www.seedtable.com/startups-london"
driver.get(target_url)

companies = driver.find_elements_by_class_name('mt-0')
all_names = [print(company.text) for company in companies]

driver.quit()   # Close Session
