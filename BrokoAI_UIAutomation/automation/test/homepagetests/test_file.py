from BrokoAI_UIAutomation.automation.src.pages.HomePage import HomePage
import allure


@allure.parent_suite("Tests for Broko AI")
@allure.suite("Tests for Home Page")
def test01_search_city_and_verify_results(set_up):
    page = set_up
    home_page = HomePage(page)
    input_string = home_page.loc_selector.__str__()
    start_index = input_string.find("xpath = (") + len("xpath = (")
    end_index = input_string.find(")")+1

    # Extract the XPath expression
    xpath_expression = input_string[start_index:end_index].strip().replace("''", "\"\"")

    print(xpath_expression)
