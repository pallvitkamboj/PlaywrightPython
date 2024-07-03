import allure
from BrokoAI_UIAutomation.automation.src.pages.HomePage import HomePage
from BrokoAI_UIAutomation.automation.src.utils.CommonFunctions import CommonFunctions
from playwright.sync_api import expect


@allure.parent_suite("Tests for Broko AI")
@allure.suite("Tests for Home Page")
def test01_search_city_and_verify_results(set_up):
    page = set_up
    try:
        location = ["Ajax", "Toronto", "Mississauga", "Brampton", "Milton", "Kitchener", "Oshawa", "Hamilton",
                    "Niagara Falls"]
        home_page = HomePage(page)
        file_path = CommonFunctions.get_project_root() + ("/BrokoAI_UIAutomation/automation/resources/login_credential"
                                                          ".json")
        credentials = CommonFunctions.read_data_from_json(file_path)
        for data in credentials:
            CommonFunctions.perform_click(page, home_page.home_page_login_button)
            CommonFunctions.do_login(page, data)
            for loc in location:
                CommonFunctions.perform_click(page, home_page.property_search_input)
                CommonFunctions.wait_for_seconds(page, 2)
                CommonFunctions.enter_value_with_delay(page, home_page.property_search_input, loc)
                CommonFunctions.press_enter(page, home_page.property_search_input)
                search_result = page.locator("xpath=.//p[text()='City']/parent::div/following-sibling::div//span["
                                             "text()=' " + loc + "']")
                CommonFunctions.wait_for_selector(page, search_result)
                CommonFunctions.perform_click(page, search_result)
                CommonFunctions.wait_for_navigation(page, "https://www.broko.ai/results")
                assert page.url == "https://www.broko.ai/results"
                if CommonFunctions.is_element_visible(page, "xpath = .//span[contains(text(),'" + loc.lower() + "')]"):
                    assert True
                else:
                    CommonFunctions.perform_click(page, home_page.property_search_input)
                    CommonFunctions.wait_for_seconds(page, 1)
                    CommonFunctions.enter_value_with_delay(page, home_page.property_search_input, loc)
                    CommonFunctions.wait_for_selector(page, search_result)
                    CommonFunctions.perform_click(page, search_result)

                CommonFunctions.wait_for_selector(page, home_page.loc_selector.nth(0))
                prop_count = home_page.loc_selector.count()
                for prop in range(0, prop_count, 1):
                    locate = home_page.loc_selector.nth(prop)
                    CommonFunctions.scroll_to_element(page, locate)
                    expect(locate).to_be_visible()
                    actual_value = CommonFunctions.get_attribute_value(page, locate, "aria-label")
                    expected_value = loc
                    CommonFunctions.assert_contains_condition(page, expected_value, actual_value, locate)
                while home_page.location_search_clear_icon.is_visible():
                    print("Clear city name button is visible")
                    page.wait_for_timeout(2000)
                    CommonFunctions.perform_click(page, home_page.location_search_clear_icon)
    finally:
        CommonFunctions.do_logout(page)


@allure.parent_suite("Tests for Broko AI")
@allure.suite("Tests for Home Page")
def test02_search_city_and_verify_results(set_up):
    page = set_up
    try:
        location = ["Mississauga"]
        home_page = HomePage(page)
        file_path = CommonFunctions.get_project_root() + ("/BrokoAI_UIAutomation/automation/resources/login_credential"
                                                          ".json")
        credentials = CommonFunctions.read_data_from_json(file_path)
        for data in credentials:
            CommonFunctions.perform_click(page, home_page.home_page_login_button)
            CommonFunctions.do_login(page, data)
            for loc in location:
                page.pause()
                CommonFunctions.wait_for_seconds(page, 5)
                CommonFunctions.wait_for_selector(page, home_page.choose_location_icon)
                CommonFunctions.perform_click(page, home_page.choose_location_icon)
                CommonFunctions.wait_for_selector(page, home_page.my_location_dropdown)
                CommonFunctions.perform_click(page, home_page.my_location_dropdown)
                location_selector = "xpath=//li[contains(text(),'" + loc + "')]"
                location_loc = page.locator(location_selector)
                CommonFunctions.perform_click(page, location_loc)
                CommonFunctions.wait_for_selector(page, home_page.close_choose_location)
                CommonFunctions.perform_click(page, home_page.close_choose_location)
                properties_near_you = ("xpath=.//h1[contains(text(),'properties near "
                                       "you')]/parent::div/following-sibling::div//h5[contains(@aria-label,"
                                       "'") + loc.lower() + "')]"
                properties_loc = page.locator(properties_near_you)
                properties_loc.nth(0).wait_for()
                properties_count = properties_loc.count()
                print(properties_count)
                for i in range(0, properties_count - 1, 1):
                    expect(properties_loc.nth(i)).to_be_visible()
                    if i == 5:
                        break
                featured_properties = ("xpath=.//h1[contains(text(),'featured "
                                       "listings')]/parent::div/following-sibling::div//h5[contains(@aria-label,"
                                       "'") + loc.lower() + "')]"
                properties_loc = page.locator(featured_properties)
                properties_loc.nth(0).wait_for()
                properties_count = properties_loc.count()
                print(properties_count)
                for i in range(0, properties_count - 1, 1):
                    expect(properties_loc.nth(i)).to_be_visible()
                    if i == 5:
                        break
    finally:
        CommonFunctions.do_logout(page)


@allure.parent_suite("Tests for Broko AI")
@allure.suite("Tests for Home Page")
def test03_search_mls_and_verify_results(set_up):
    page = set_up
    try:
        location = ["W8416836", "W8390590", "W7332526", "W8489174", "E6566321", "E6316621", "N6334658", "N6319073",
                    "X6178936", "X5947275"]
        home_page = HomePage(page)
        file_path = CommonFunctions.get_project_root() + ("/BrokoAI_UIAutomation/automation/resources/login_credential"
                                                          ".json")
        credentials = CommonFunctions.read_data_from_json(file_path)
        for data in credentials:
            CommonFunctions.perform_click(page, home_page.home_page_login_button)
            CommonFunctions.do_login(page, data)
            for loc in location:
                CommonFunctions.perform_click(page, home_page.property_search_input)
                CommonFunctions.wait_for_seconds(page, 2)
                CommonFunctions.enter_value_with_delay(page, home_page.property_search_input, loc)
                CommonFunctions.press_enter(page, home_page.property_search_input)
                search_result = page.locator("xpath=.//p[text()='MLS']/parent::div/following-sibling::div//span["
                                             "text()=' " + loc + "']")
                CommonFunctions.wait_for_selector(page, search_result)
                CommonFunctions.perform_click(page, search_result)
                CommonFunctions.wait_for_navigation(page, "https://www.broko.ai/results")
                assert page.url == "https://www.broko.ai/results"
                CommonFunctions.wait_for_selector(page, home_page.loc_selector.nth(0))
                prop_count = home_page.loc_selector.count()
                for prop in range(0, prop_count, 1):
                    CommonFunctions.scroll_to_element(page, home_page.loc_selector.nth(prop))
                    expect(home_page.loc_selector.nth(prop)).to_be_visible()
                while home_page.location_search_clear_icon.is_visible():
                    print("Clear city name button is visible")
                    page.wait_for_timeout(2000)
                    CommonFunctions.perform_click(page, home_page.location_search_clear_icon)
    finally:
        CommonFunctions.do_logout(page)
