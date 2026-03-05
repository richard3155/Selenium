import logging
from selenium import webdriver
from selenium.webdriver.common.by import By

logging.basicConfig(
    filename="buyer.log",
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logging.info("Старт скрипта")

try:
    driver = webdriver.Chrome()
    logging.info("Браузер запущен")
except Exception:
    logging.critical("Не удалось запустить браузер")
    exit()

product_url = "https://store.steampowered.com/app/730/CounterStrike_Global_Offensive/"
logging.info(f"Переход на страницу товара: {product_url}")
driver.get(product_url)

try:
    text = driver.find_element(By.TAG_NAME, "body").text.lower()
    logging.debug("Страница прочитана")

    if "not available" in text or "unavailable" in text:
        logging.warning("Товар недоступен")
    else:
        logging.info("Товар доступен")

except Exception:
    logging.error("Ошибка при проверке товара")

input("Нажмите Enter для выхода...")
driver.quit()
logging.info("Скрипт завершён")
