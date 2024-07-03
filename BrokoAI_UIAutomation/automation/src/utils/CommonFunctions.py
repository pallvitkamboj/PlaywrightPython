import json
import os
from datetime import datetime

import allure

from BrokoAI_UIAutomation.automation.src.pages.HomePage import HomePage
from BrokoAI_UIAutomation.automation.src.pages.LoginPage import LoginPage


class CommonFunctions:
    now = datetime.now()
    dt_string = now.strftime("%d_%m_%y_%H%M%S")
    date_str = now.strftime("%d_%m_%Y")
    screenshot_path = "\\screenshots\\" + date_str + "\\" + dt_string + ".png"

    @staticmethod
    def do_login(page, credentials):
        try:
            login_p = LoginPage(page)
            with allure.step("Logging In with " + credentials['email'] + " tenant = " + credentials['tenant']):
                CommonFunctions.enter_value(page, login_p.inputUsername, credentials['email'])
                CommonFunctions.enter_value(page, login_p.inputPassword, credentials['pass'])
                CommonFunctions.perform_click(page, login_p.loginButton)
        except Exception as e:
            path = CommonFunctions.get_project_root() + CommonFunctions.screenshot_path
            page.screenshot(path=path)
            print(e, " Screen shot captured. " + "Unable to login")
            allure.attach(path, name="Screenshot", attachment_type=allure.attachment_type.PNG)
            assert False, e.__str__() + " Unable to login"

    @staticmethod
    def do_logout(page):
        try:
            with allure.step("Logging out"):
                home_p = HomePage(page)
                CommonFunctions.perform_click(page, home_p.profile_icon)
                CommonFunctions.perform_click(page, home_p.sign_out_button)
        except Exception as e:
            path = CommonFunctions.get_project_root() + CommonFunctions.screenshot_path
            page.screenshot(path=path)
            print(e, " Screen shot captured. " + "Unable to logout")
            allure.attach(path, name="Screenshot", attachment_type=allure.attachment_type.PNG)
            assert False, e.__str__() + " Unable to logout"

    @staticmethod
    def perform_click(page, locator):
        try:
            with allure.step("Clicking on " + str(locator)):
                locator.click()
        except Exception as e:
            path = CommonFunctions.get_project_root() + CommonFunctions.screenshot_path
            page.screenshot(path=path)
            print(e, " Screen shot captured. " + "Unable to click on ", str(locator))
            allure.attach(path, name="Screenshot", attachment_type=allure.attachment_type.PNG)
            assert False, e.__str__() + " Unable to click on " + str(locator)

    @staticmethod
    def get_text(page, locator):
        try:
            with allure.step("Fetching text of " + str(locator)):
                return locator.inner_text()
        except Exception as e:
            path = CommonFunctions.get_project_root() + CommonFunctions.screenshot_path
            page.screenshot(path=path)
            print(path)
            print(e, " Screen shot captured. " + "Unable to get text of " + str(locator))
            allure.attach(path, name="Screenshot", attachment_type=allure.attachment_type.PNG)
            assert False, e.__str__() + " Unable to get text of " + str(locator)

    @staticmethod
    def enter_value(page, locator, value):
        try:
            with allure.step("Entering value " + value + " in " + str(locator)):
                locator.clear()
                locator.fill(value)
        except Exception as e:
            path = CommonFunctions.get_project_root() + CommonFunctions.screenshot_path
            page.screenshot(path=path)
            print(e, " Screen shot captured. " + "Unable to enter value ", value, " in element ", str(locator))
            allure.attach(path, name="Screenshot", attachment_type=allure.attachment_type.PNG)
            assert False, e.__str__() + " Unable to enter value " + value + " in element " + str(locator)

    @staticmethod
    def read_data_from_json(file_name):
        try:
            with open(file_name, "r") as file:
                data_list = json.load(file)
                return data_list
        except Exception as e:
            print(e, " Screen shot captured. " + "Unable to read data from json")
            assert False, e.__str__() + " Unable to read data from json"

    @staticmethod
    def get_project_root():
        try:
            current_dir = os.getcwd()
            while not os.path.exists(os.path.join(current_dir, 'readme.txt')):
                current_dir = os.path.dirname(current_dir)
                if current_dir == os.path.dirname(current_dir):
                    raise FileNotFoundError(
                        "Marker file 'readme.txt' not found. Are you sure you're in the project directory?")
            return current_dir
        except Exception as e:
            print(e, " Screen shot captured. " + "Unable to get project root path")
            assert False, e.__str__() + " Unable to get project root path"

    @staticmethod
    def wait_for_navigation(page, url):
        try:
            with allure.step("Waiting for url " + url):
                page.wait_for_url(url)
        except Exception as e:
            path = CommonFunctions.get_project_root() + CommonFunctions.screenshot_path
            page.screenshot(path=path)
            print(e, " Screen shot captured. " + "Wait for navigation to new URL failed")
            allure.attach(path, name="Screenshot", attachment_type=allure.attachment_type.PNG)
            assert False, e.__str__() + " Wait for navigation to new URL failed"

    @staticmethod
    def wait_for_selector(page, locator):
        try:
            with allure.step("Waiting for selector " + str(locator)):
                locator.wait_for()
        except Exception as e:
            path = CommonFunctions.get_project_root() + CommonFunctions.screenshot_path
            page.screenshot(path=path)
            print(e, " Screen shot captured. " + "Wait for selector failed")
            allure.attach(path, name="Screenshot", attachment_type=allure.attachment_type.PNG)
            assert False, e.__str__() + " Wait for selector failed"

    @staticmethod
    def get_attribute_value(page, locator, attribute):
        try:
            with allure.step("Fetching attribute value of " + attribute):
                return locator.get_attribute(attribute)
        except Exception as e:
            path = CommonFunctions.get_project_root() + CommonFunctions.screenshot_path
            page.screenshot(path=path)
            print(e, " Screen shot captured. " + "Unable to get attribute value of ", str(locator))
            allure.attach(path, name="Screenshot", attachment_type=allure.attachment_type.PNG)
            assert False, e.__str__() + " Unable to get attribute value of " + str(locator)

    @staticmethod
    def wait_for_seconds(page, time):
        try:
            with allure.step("Waiting for seconds " + time.__str__()):
                page.wait_for_timeout(time * 1000)
        except Exception as e:
            path = CommonFunctions.get_project_root() + CommonFunctions.screenshot_path
            page.screenshot(path=path)
            print(e, " Screen shot captured. " + "Wait Failed !!!")
            allure.attach(path, name="Screenshot", attachment_type=allure.attachment_type.PNG)
            assert False, e.__str__() + " Wait Failed !!!"

    @staticmethod
    def navigate_forward_if_next_page_available(page):
        try:
            with allure.step("Navigating to the Next page"):
                page.go_forward()
        except Exception as e:
            path = CommonFunctions.get_project_root() + CommonFunctions.screenshot_path
            page.screenshot(path=path)
            print(e, "Next Page not available")
            allure.attach(path, name="Screenshot", attachment_type=allure.attachment_type.PNG)
            assert False, e.__str__() + " Next Page not available"

    @staticmethod
    def go_back(page):
        try:
            with allure.step("Navigating to the previous page"):
                page.go_back()
        except Exception as e:
            path = CommonFunctions.get_project_root() + CommonFunctions.screenshot_path
            page.screenshot(path=path)
            print(e, "Not able to Navigate on the previous page")
            allure.attach(path, name="Screenshot", attachment_type=allure.attachment_type.PNG)
            assert False, e.__str__() + " Not able to Navigate on the previous page"

    @staticmethod
    def navigate_to_url(page, url):
        try:
            with allure.step("Navigating to the " + url):
                page.goto(url)
        except Exception as e:
            path = CommonFunctions.get_project_root() + CommonFunctions.screenshot_path
            page.screenshot(path=path)
            print(e, "Not able to Navigate on the " + url)
            allure.attach(path, name="Screenshot", attachment_type=allure.attachment_type.PNG)
            assert False, e.__str__() + " Not able to Navigate on the " + url

    @staticmethod
    def scroll_to_element(page, element):
        try:
            with allure.step("Scroll to element " + element.__str__()):
                element.scroll_into_view_if_needed()
        except Exception as e:
            path = CommonFunctions.get_project_root() + CommonFunctions.screenshot_path
            page.screenshot(path=path)
            print(e, "Not able to Scroll to element " + element.__str__())
            allure.attach(path, name="Screenshot", attachment_type=allure.attachment_type.PNG)
            assert False, e.__str__() + " Not able to Scroll to element " + element.__str__()

    @staticmethod
    def assert_contains_condition(page, expected_value, actual_value, locator):
        try:
            with allure.step("Assert contains condition " + expected_value + " in " + actual_value):
                assert expected_value in actual_value
        except AssertionError as e:
            path = CommonFunctions.get_project_root() + CommonFunctions.screenshot_path
            CommonFunctions.evaluate_js_for_ss(page, locator)
            page.screenshot(path=path)
            with open(path, 'rb') as image:
                file = image.read()
                byte_array = bytearray(file)
                print(e, "Assertion Failed " + actual_value + " does not contains " + expected_value)
                allure.attach(byte_array, name="Screenshot", attachment_type=allure.attachment_type.PNG)
            assert False, e.__str__() + "Assertion Failed " + actual_value + " does not contains " + expected_value

    @staticmethod
    def is_element_visible(page, element):
        try:
            with allure.step("Verify if element is present " + element.__str__()):
                return page.locator(element).count() > 0
        except Exception as e:
            path = CommonFunctions.get_project_root() + CommonFunctions.screenshot_path
            page.screenshot(path=path)
            print(e, "Unable to verify the presence of element " + element.__str__())
            allure.attach(path, name="Screenshot", attachment_type=allure.attachment_type.PNG)
            assert False, e.__str__() + "Unable to verify the presence of element " + element.__str__()

    @staticmethod
    def press_enter(page, element):
        try:
            with allure.step("Press enter key on " + element.__str__()):
                page.keyboard.press("Enter")
        except Exception as e:
            path = CommonFunctions.get_project_root() + CommonFunctions.screenshot_path
            page.screenshot(path=path)
            print(e, "Press enter key failed on " + element.__str__())
            allure.attach(path, name="Screenshot", attachment_type=allure.attachment_type.PNG)
            assert False, e.__str__() + "Press enter key failed on " + element.__str__()

    @staticmethod
    def enter_value_with_delay(page, locator, value):
        try:
            with allure.step("Entering value with delay " + value + " in " + str(locator)):
                locator.clear()
                locator.type(value, delay=50)
        except Exception as e:
            path = CommonFunctions.get_project_root() + CommonFunctions.screenshot_path
            page.screenshot(path=path)
            print(e, "Screen shot captured. " + "Unable to enter value with delay ", value, " in element ",
                  str(locator))
            allure.attach(path, name="Screenshot", attachment_type=allure.attachment_type.PNG)
            assert False, e.__str__() + " Unable to enter value with delay " + value + " in element " + str(locator)

    @staticmethod
    def evaluate_js_for_ss(page, locator):
        try:
            locator = locator.__str__()
            start_index = locator.find("xpath = (.") + len("xpath = (.")
            end_index = locator.find(")") + 1
            xpath_expression = locator[start_index:end_index].strip().replace("''", "\"\"")
            print(xpath_expression)
            js_code = f'''
                        const xpathExpression = '{xpath_expression}';
                        const element = document.evaluate(xpathExpression, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
                        if (element) {{
                            element.style.border = '2px solid red';
                        }}
                    '''
            page.evaluate(js_code)
        except Exception as e:
            print(e.__str__() + " Function evaluate_js_for_ss failed")
