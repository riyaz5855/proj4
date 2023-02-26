from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.shiprocket.in/shipping-rate-calculator/")

# Enter source and destination pincode
source_pincode = driver.find_element(By.XPATH, '//*[@id="domesticPickupPincode"]')
source_pincode.send_keys("110001")

destination_pincode = driver.find_element(By.XPATH, '//*[@id="domesticDeliveryPincode"]')
destination_pincode.send_keys("110011")

time.sleep(10)
# Click the calculate button
calculate_button = driver.find_element(By.XPATH, '//*[@class="domesticButton"]')
calculate_button.click()

# Wait for the table to load
time.sleep(10)


element = driver.find_element("xpath", '/html/body/section[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div[1]/div/table/tbody/tr[1]/td[4]')
value = element.text
print("-----------------------------------------------------")
print("Value of element:", value)
print("Value of element:", element)
# Find the table using xpath
# table = driver.find_element(By.XPATH, "/html/body/section[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div[1]/div/table/tbody")

# Get the data from the table
# data = table.text
# rows = table.find_elements_by_xpath(".//tr")
# for row in rows:
#     cells = row.find_elements_by_xpath(".//td")
#     row_data = []
#     for cell in cells:
#         row_data.append(cell.text)
#     print(row_data)

# Print the data
# print(data)

driver.quit()
