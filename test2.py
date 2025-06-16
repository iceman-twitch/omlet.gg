import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


PROXY = "88.198.24.108:8080" # IP:PORT or HOST:PORT

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--proxy-server=%s' % PROXY)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ifconfig.me/")
driver.find_element_by_xpath("/html/body").send_keys(Keys.CONTROL + 't')
driver.execute_script("window.open('https://www.croxyproxy.com/', '_blank');") 

time.sleep(2) 
windows = driver.window_handles

time.sleep(2)
driver.switch_to.window(windows[1])

url= "https://omlet.gg/stream/username"
driver.execute_script(f'var element = document.getElementById("url"); element.value = "{  url }";')
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="requestSubmit"]' ))).click() 
print("CHECK")