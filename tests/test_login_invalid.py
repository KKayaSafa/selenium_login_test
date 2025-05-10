from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
import time
import os

def test_invalid_login():
    # Tarayıcı ayarları
    options = Options()
    #options.add_argument("--headless")  # İsteğe bağlı: Tarayıcı arayüzü olmadan çalıştırmak için
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1800, 1200)  # veya driver.maximize_window()


    try:
        # Login sayfasına git
        driver.get("https://the-internet.herokuapp.com/login")

        # Kullanıcı adı ve şifre alanlarını doldur
        username = driver.find_element(By.ID, "username")
        password = driver.find_element(By.ID, "password")
        username.send_keys("wronguser")
        password.send_keys("wrongpass")
        password.send_keys(Keys.RETURN)

        time.sleep(2)  # Sayfanın yüklenmesini bekle

        # Hata mesajını kontrol et
        error = driver.find_element(By.ID, "flash").text
        assert "Your username is invalid!" in error


    except AssertionError:
        print("Test başarısız: Hata mesajı beklenilen gibi değil.")
    finally:
        time.sleep(30)
        driver.quit()

if __name__ == "__main__":
    test_invalid_login()
