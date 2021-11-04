from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# 1
my_driver = webdriver.Chrome(executable_path="/Users/adirremi/Desktop/chromedriver")
my_driver.get("https://www.mako.co.il")

# 2
web_title = my_driver.title
my_driver.refresh()
if web_title == my_driver.title:
    print("same after refresh")
else:
    print("oh title is been changed")

# 4
my_driver = webdriver.Chrome(executable_path="/Users/adirremi/Desktop/chromedriver")
my_driver.get("https://translate.google.co.il/?hl=iw")
my_driver.find_element_by_xpath(
    "//*[@id=\"yDmH0d\"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/span/span/div/textarea").send_keys(
    "אהלן מיקו")

# 5
my_driver = webdriver.Chrome(executable_path="/Users/adirremi/Desktop/chromedriver")
my_driver.get("https://youtube.com")

WebDriverWait(my_driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#search"))).send_keys(
    "the paper kite bloom")
my_driver.find_element_by_css_selector("button.style-scope.ytd-searchbox#search-icon-legacy").click()

# 6
my_driver.get("https://translate.google.com")

my_driver = webdriver.Chrome(executable_path="/Users/adirremi/Desktop/chromedriver")
my_driver.get("https://translate.google.com")

locOne = my_driver.find_element_by_class_name("er8xn").send_keys("haha ")
locTwo = my_driver.find_element_by_tag_name("textarea").send_keys("ze oved ")
locThree = my_driver.find_element_by_xpath(
    "//*[@id=\"yDmH0d\"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/span/span/div/textarea").send_keys(
    "aviel")

# 7
my_driver = webdriver.Chrome(executable_path="/Users/adirremi/Desktop/chromedriver")
my_driver.get("https://facebook.com")

my_driver.find_element_by_css_selector("input#email ").send_keys("UrName")
my_driver.find_element_by_css_selector("input#pass ").send_keys("UrPass")
nextButt = my_driver.find_element_by_name("login")

nextButt.click()

# 8

my_driver = webdriver.Chrome(executable_path="/Users/adirremi/Desktop/chromedriver")
my_driver.get("https://facebook.com")

print(my_driver.get_cookies())
my_driver.delete_all_cookies()
print("2")
print(my_driver.get_cookies())

# 9
my_driver = webdriver.Chrome(executable_path="/Users/adirremi/Desktop/chromedriver")
my_driver.get("https://github.com")
my_driver.find_element_by_name("q").send_keys("selenuim" + Keys.ENTER)

# 10
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
browser = webdriver.Chrome(executable_path="/Users/adirremi/Desktop/chromedriver", chrome_options=chrome_options)
browser.get("https://walla.co.il")
