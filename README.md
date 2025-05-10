# 🔐 Selenium Login Testi

Bu proje, basit bir login sayfası için Selenium kullanılarak yazılmış bir otomasyon testidir. Hatalı kullanıcı adı ve şifre ile giriş yapıldığında hata mesajının doğru şekilde görünüp görünmediğini test eder.

---

## 🧪 Test Senaryosu

1. Chrome tarayıcısı başlatılır.
2. Login sayfasına gidilir: [https://the-internet.herokuapp.com/login](https://the-internet.herokuapp.com/login)
3. Hatalı kullanıcı adı ve şifre girilir.
4. "Your username is invalid!" hata mesajının görüntülenip görüntülenmediği kontrol edilir.
5. Tarayıcı 30 saniye açık kalır, ardından kapanır.

---

## 🧰 Gereksinimler

- Python 3.7+
- Google Chrome (yüklü olmalı)
- ChromeDriver (PATH'e eklenmiş olmalı)

### Gerekli Python Paketleri

```bash
pip install selenium
