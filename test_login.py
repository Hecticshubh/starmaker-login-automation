from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# TC_01: Login page opens

def test_login_page_opens(driver, wait):
    driver.get("https://www.starmakerstudios.com/en/web-login")

    wait.until(lambda d: "/web-login" in d.current_url)
    wait.until(lambda d: d.title.strip() != "")

    assert "/web-login" in driver.current_url
    assert driver.title.strip() != ""


# TC_02: Valid login

def test_valid_login(driver, wait):
    driver.get("https://www.starmakerstudios.com/en/web-login")

    email = wait.until(
        EC.visibility_of_element_located((By.ID, "email"))
    )
    password = wait.until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    login_button = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[type='submit']")
        )
    )

    email.send_keys("poleduqy@polkaroad.net")
    password.send_keys("Avengers1")
    login_button.click()

    profile = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "img[alt='avatar']")
        )
    )
    assert profile.is_displayed()


# TC_03: Email field visible and enabled

def test_email_field_visible(driver, wait):
    driver.get("https://www.starmakerstudios.com/en/web-login")

    email = wait.until(
        EC.visibility_of_element_located((By.ID, "email"))
    )
    assert email.is_displayed()
    assert email.is_enabled()


# TC_04: Password field visible and enabled

def test_password_field_visible(driver, wait):
    driver.get("https://www.starmakerstudios.com/en/web-login")

    password = wait.until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    assert password.is_displayed()
    assert password.is_enabled()


# TC_05: Both fields blank

def test_blank_login(driver, wait):
    driver.get("https://www.starmakerstudios.com/en/web-login")

    login_button = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[type='submit']")
        )
    )
    login_button.click()

    errors = wait.until(
        EC.visibility_of_all_elements_located(
            (By.CSS_SELECTOR, ".ant-form-item-explain-error")
        )
    )
    messages = [error.text for error in errors]

    assert "Invalid email" in messages
    assert "Wrong password" in messages


# TC_06: Valid email and blank password

def test_valid_email_blank_password(driver, wait):
    driver.get("https://www.starmakerstudios.com/en/web-login")

    email = wait.until(
        EC.visibility_of_element_located((By.ID, "email"))
    )
    email.send_keys("poleduqy@polkaroad.net")

    login_button = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[type='submit']")
        )
    )
    login_button.click()

    error = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//div[contains(@class,'ant-form-item-explain-error') "
                "and normalize-space()='Wrong password']"
            )
        )
    )
    assert error.text == "Wrong password"


# TC_07: Blank email and password filled

def test_blank_email_valid_password(driver, wait):
    driver.get("https://www.starmakerstudios.com/en/web-login")

    password = wait.until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    password.send_keys("Avengers1")

    login_button = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[type='submit']")
        )
    )
    login_button.click()

    error = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//div[contains(@class,'ant-form-item-explain-error') "
                "and normalize-space()='Invalid email']"
            )
        )
    )
    assert error.text == "Invalid email"


# TC_08: Invalid email and invalid password

def test_invalid_email_password(driver, wait):
    driver.get("https://www.starmakerstudios.com/en/web-login")

    email = wait.until(
        EC.visibility_of_element_located((By.ID, "email"))
    )
    email.send_keys("invalid123@example.com")

    password = wait.until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    password.send_keys("WrongPass123")

    login_button = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[type='submit']")
        )
    )
    login_button.click()

    error = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//div[contains(@class,'ant-form-item-explain-error') "
                "and normalize-space()='Account is not found. Create one in StarMaker App.']"
            )
        )
    )
    assert error.text == "Account is not found. Create one in StarMaker App."


# TC_09: Valid email and wrong password

def test_valid_email_wrong_password(driver, wait):
    driver.get("https://www.starmakerstudios.com/en/web-login")

    email = wait.until(
        EC.visibility_of_element_located((By.ID, "email"))
    )
    email.send_keys("poleduqy@polkaroad.net")

    password = wait.until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    password.send_keys("WrongPass123")

    login_button = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[type='submit']")
        )
    )
    login_button.click()

    error = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//span[normalize-space()='Username or password is incorrect']"
            )
        )
    )
    assert error.is_displayed()
    assert error.text == "Username or password is incorrect"


# TC_10: Password masking

def test_password_masking(driver, wait):
    driver.get("https://www.starmakerstudios.com/en/web-login")

    password = wait.until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    assert password.get_attribute("type") == "password"