from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")


# Inicializa el navegador
driver = webdriver.Chrome()
url = 'https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?'
name_of_table = 'cumulative'
spicifi_table = 'table=' + name_of_table
url = url + spicifi_table

driver.get(url)

try:
    input("Press Enter to exit web...")
except:
    print('No se encontro la tabla')


