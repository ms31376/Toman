import pytest
from pages.login_page import LoginPage
import configs


@pytest.mark.parametrize(("phone_number"),
                         [(configs.credentials['user1']['phone_number'])])

def test_user_login_with_sms(init_driver, phone_number):
    login_page = LoginPage(init_driver)
    login_page.open_login_page()
    login_page.login_with_sms(phone_number)
    login_page.go_to_profile()
    profile_url = "https://www.digikala.com/profile/"
    assert profile_url == init_driver.current_url, f"Expected URL to be {profile_url}, but got {init_driver.current_url}"
@pytest.mark.parametrize("email, password", [
    (configs.credentials['user2']['email'], configs.credentials['user2']['password'])
])
def test_user_login_with_email(init_driver, email, password):
    login_page = LoginPage(init_driver)
    login_page.open_login_page()
    login_page.login_with_email(email, password)
    login_page.go_to_profile()
    profile_url = "https://www.digikala.com/profile/"
    assert profile_url == init_driver.current_url, f"Expected URL to be {profile_url}, but got {init_driver.current_url}"

@pytest.mark.parametrize("email, password", [
    (user['email'], user['password']) for user in configs.credentials['invalid_users']
])
def test_user_login_with_invalid_email(init_driver, email, password):
    login_page = LoginPage(init_driver)
    login_page.open_login_page()
    toast = login_page.login_with_email(email, password).strip()
    assert "حساب کاربری با مشخصات" in toast or "بیشتر از حد مجاز" in toast, \
        f"Expected toast message to contain 'ایمیل در سیستم وجود نداره' or 'بیشتر از حد مجاز تلاش کرده‌اید', but got: {toast}"