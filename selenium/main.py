from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time

PATH = "C:\\Program Files (x86)\\chromedriver.exe"  # Use double backslashes for Windows paths
service = Service(PATH)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.youtube.com")

# Search for "hello world"
search = driver.find_element(By.NAME, "search_query")
search.send_keys("hello world")
search.send_keys(Keys.RETURN)

try:
    # Wait for video results to load
    videos = WebDriverWait(driver, 15).until(
        EC.presence_of_all_elements_located((By.XPATH, '//ytd-video-renderer'))
    )

    print("\nScraped Video Data:\n")

    for video in videos:
        try:
            title_element = video.find_element(By.ID, "video-title")
            title = title_element.text
            link = title_element.get_attribute("href")
            channel = video.find_element(By.ID,"channel-name").text
            print(f"Title: {title}")
            print(f"Link: {link}\n")
            print(f"Channel: {channel}\n")
        except Exception as e:
            continue  # Skip incomplete/irregular entries

finally:
    print("\nScraping Completed.\n")

time.sleep(5)
driver.quit()
