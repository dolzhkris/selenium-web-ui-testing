from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.support.ui import Select
import time
import traceback

def users():
    return [standard_user, locked_out_user, problem_user, performance_glitch_user, error_user,  visual_user]

def safe_execute(driver, func, *args, **kwargs):
    try:
        func(driver, *args, **kwargs)
        return True
    except Exception as e:
        print(f"Ошибка в функции {func.__name__}: {str(e)}")
        traceback.print_exc()  # Печать полной трассировки ошибки
        return False

def spisok(driver):
    sort_values = ["za", "lohi", "hilo", "az"]
    for value in sort_values:
        dropdown_element = driver.find_element(By.CLASS_NAME, "product_sort_container")
        dropdown = Select(dropdown_element)
        dropdown.select_by_value(value)
        time.sleep(2)

def menu(driver):
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    time.sleep(1)
    menu_items = ["inventory_sidebar_link", "reset_sidebar_link", "about_sidebar_link", "logout_sidebar_link"]
    for item in menu_items:
        if item == "reset_sidebar_link" or item == "inventory_sidebar_link":
            driver.find_element(By.ID, item).click()
            time.sleep(1)
        if item == "about_sidebar_link":
            driver.find_element(By.ID, item).click()
            time.sleep(2)
            driver.back()
            time.sleep(1)
            driver.find_element(By.ID, "react-burger-menu-btn").click()
            time.sleep(1)
        if item == "logout_sidebar_link":
            driver.find_element(By.ID, item).click()
            time.sleep(1)
            
def cart_test(driver):
    product_ids = ["sauce-labs-backpack", "sauce-labs-bike-light", "sauce-labs-bolt-t-shirt",
    "sauce-labs-fleece-jacket", "sauce-labs-onesie", "test.allthethings()-t-shirt-(red)"]
    for product_id in product_ids:
        add_cart = f"add-to-cart-{product_id}"
        driver.find_element(By.ID, add_cart).click()
        time.sleep(0.5)
    for product_id in product_ids:
        remove_cart = f"remove-{product_id}"
        driver.find_element(By.ID, remove_cart).click()
        time.sleep(0.5)

def test_web(driver):
    try:
        time.sleep(0.5)
        driver.find_element(By.ID, "login-button").click() #Поле ввода пароля
        spisok(driver)
        cart_test(driver)
        driver.find_element(By.ID, "shopping_cart_container").click()
        time.sleep(1)
        driver.back()
        time.sleep(0.5)
        product_ids = ["sauce-labs-backpack", "sauce-labs-bike-light", "sauce-labs-bolt-t-shirt",
        "sauce-labs-fleece-jacket", "sauce-labs-onesie", "test.allthethings()-t-shirt-(red)"]
        for product_id in product_ids:
            add_cart = f"add-to-cart-{product_id}"
            driver.find_element(By.ID, add_cart).click()
            time.sleep(0.5)
        driver.find_element(By.ID, "shopping_cart_container").click()
        time.sleep(2)
        for product_id in product_ids:
            remove_cart = f"remove-{product_id}"
            driver.find_element(By.ID, remove_cart).click()
            time.sleep(0.5)
        driver.find_element(By.ID, "continue-shopping").click()
        time.sleep(1)
        driver.back()
        time.sleep(1)
        driver.find_element(By.ID, "checkout").click()
        time.sleep(1)
        driver.find_element(By.ID, "continue").click()
        time.sleep(1)
        checkout_items = ["first-name", "last-name", "postal-code"]
        checkout_values = ["Kris", "Dolzh", "120000"]
        for item, value in zip(checkout_items, checkout_values):
            driver.find_element(By.ID, item).clear()
            time.sleep(0.5)
            driver.find_element(By.ID, item).send_keys(value)
            time.sleep(0.5)
            driver.find_element(By.ID, "continue").click()
            time.sleep(1)
        driver.find_element(By.ID, "finish").click()
        time.sleep(1)
        driver.find_element(By.ID, "back-to-products").click()
        time.sleep(1)
        driver.back()
        time.sleep(1)
        driver.back()
        time.sleep(1)
        driver.find_element(By.ID, "cancel").click()
        time.sleep(1)
        menu(driver)
    except Exception as e:
        print(f"Ошибка в standard_user: {e}")
        raise  # Пробрасываем исключение дальше

def standard_user(driver):
    driver.find_element(By.ID, "user-name").clear() 
    time.sleep(0.5)
    driver.find_element(By.ID, "user-name").send_keys('standard_user')
    time.sleep(0.5)
    driver.find_element(By.ID, "password").clear()
    time.sleep(0.5)
    driver.find_element(By.ID, "password").send_keys('secret_sauce')

def locked_out_user(driver):
    driver.find_element(By.ID, "user-name").clear() 
    time.sleep(0.5)
    driver.find_element(By.ID, "user-name").send_keys('locked_out_user')
    time.sleep(0.5)
    driver.find_element(By.ID, "password").clear()
    time.sleep(0.5)
    driver.find_element(By.ID, "password").send_keys('secret_sauce')

def problem_user(driver):
    driver.find_element(By.ID, "user-name").clear() 
    time.sleep(0.5)
    driver.find_element(By.ID, "user-name").send_keys('problem_user')
    time.sleep(0.5)
    driver.find_element(By.ID, "password").clear()
    time.sleep(0.5)
    driver.find_element(By.ID, "password").send_keys('secret_sauce')

def performance_glitch_user(driver):
    driver.find_element(By.ID, "user-name").clear() 
    time.sleep(0.5)
    driver.find_element(By.ID, "user-name").send_keys('performance_glitch_user')
    time.sleep(0.5)
    driver.find_element(By.ID, "password").clear()
    time.sleep(0.5)
    driver.find_element(By.ID, "password").send_keys('secret_sauce')

def error_user(driver):
    driver.find_element(By.ID, "user-name").clear() 
    time.sleep(0.5)
    driver.find_element(By.ID, "user-name").send_keys('error_user')
    time.sleep(0.5)
    driver.find_element(By.ID, "password").clear()
    time.sleep(0.5)
    driver.find_element(By.ID, "password").send_keys('secret_sauce')

def visual_user(driver):
    driver.find_element(By.ID, "user-name").clear() 
    time.sleep(0.5)
    driver.find_element(By.ID, "user-name").send_keys('visual_user')
    time.sleep(0.5)
    driver.find_element(By.ID, "password").clear()
    time.sleep(0.5)
    driver.find_element(By.ID, "password").send_keys('secret_sauce')

def test():
    for test_func in users():
        print(f"\nЗапуск теста: {test_func.__name__}")
        driver = None
        try:
            driver = webdriver.Edge()
            driver.maximize_window()
            driver.implicitly_wait(5)
            driver.get("https://www.saucedemo.com/")
            safe_execute(driver, test_func)
            test_web(driver)

        except Exception as e:
            print(f"Критическая ошибка в {test_func.__name__}: {e}")
        finally:
            if driver is not None:
                try:
                    driver.quit()
                    time.sleep(1)
                except:
                    print("Ошибка при закрытии драйвера")

if __name__ == "__main__":
    test()
