from seleniumbase import BaseCase, drivers


class MyTestClass(BaseCase):

    def test_example(self):
        self.open("https://www.shiprocket.in/shipping-rate-calculator/")
        self.update_text("input#domesticPickupPincode", "400037")
        self.update_text("input#domesticDeliveryPincode", "400028")
        self.click(".domesticButton button")

        self.sleep(2)
        table_data = self.find_element_by_xpath("/html/body/section[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div[1]/div/table/tbody")
        rows = table_data.find_elements_by_xpath(".//tr")
        for row in rows:
            print("maa ki aankh")
            cells = row.find_elements_by_xpath(".//td")
            row_data = []
            for cell in cells:
                row_data.append(cell.text)
            print(row_data)

        self.sleep(10)