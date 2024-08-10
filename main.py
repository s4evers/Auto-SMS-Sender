from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import time

def read_numbers_from_file(filename):
    with open(filename, 'r') as file:
        numbers = [line.strip() for line in file.readlines()]
    return numbers

def main():
    chrome_options = Options()
    chrome_options.add_extension("buster.crx")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0")

    numbers = read_numbers_from_file("requirements.txt")

    for number in numbers:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

        try:
            driver.get("https://bulksms.com/test")
            time.sleep(5)

            try:
                accept_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary accept-all']"))
                )
                accept_button.click()
            except TimeoutException:
                print("Qabul qilish tugmasi topilmadi yoki bosilmaydi.")
                driver.quit()
                continue

            time.sleep(3)

            try:
                number_input = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.ID, 'cell_number'))
                )
                number_input.send_keys(f'+48{number}')
            except TimeoutException:
                print("Raqam kiritish maydoni topilmadi yoki bosilmaydi.")
                driver.quit()
                continue

            time.sleep(3)

            try:
                send_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "#send-message-btn"))
                )
                send_button.click()
            except TimeoutException:
                print("Yuborish tugmasi topilmadi yoki bosilmaydi.")
                driver.quit()
                continue

            time.sleep(2)

            driver.switch_to.default_content()

            try:
                iframe_challenge = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//iframe[@title="recaptcha challenge expires in two minutes"]'))
                )
                driver.switch_to.frame(iframe_challenge)
                time.sleep(3)

                buster_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="rc-imageselect"]/div[3]/div[2]/div[1]/div[1]/div[4]'))
                )
                buster_button.click()
                time.sleep(5)

                driver.switch_to.default_content()

            except TimeoutException:
                print("Buster tugmasi topilmadi yoki bosilmaydi.")
                time.sleep(2)
                driver.quit()
                continue

            print("Buster tugmasi bosildi. Uzoq vaqt kutish.")
            time.sleep(5)

        except Exception as e:
            print(f"Xatolik: {e}")

        finally:
            driver.quit()

if __name__ == "__main__":
    main()
