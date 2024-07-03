class HomePage:

    def __init__(self, page):
        self.page = page
        self.home_page_login_button = page.get_by_role("button", name="LOGIN")
        self.profile_icon = page.locator("xpath=//div[@class='profile_name']")
        self.sign_out_button = page.locator("xpath=//button[text()='sign out']")
        self.property_search_input = page.get_by_placeholder("Enter Location, MLS or Postal")
        self.location_search_first_option = page.locator("xpath=(//div[@class='location_wrp_inner']/p)[1]")
        self.results_text = page.locator("xpath=//div[@class='results_heading_flx']/span")
        self.choose_location_icon = page.locator("#current_simulation_icon_wrp")
        self.close_choose_location = page.get_by_test_id("KeyboardDoubleArrowRightIcon")
        self.my_location_dropdown = page.locator("xpath=//div[text()='My Location']")
        self.broko_header_icon = page.locator("xpath=//div[@class='haeder_wrp_flx']//img[@alt='broko_v1_logo']")
        self.location_search_clear_icon = page.locator("xpath=//div[@class='searchInnerWrp']//*[local-name()='svg' "
                                                       "and @data-testid='CancelIcon']")
        self.loc_selector = page.locator("xpath = (.//h5[contains(@aria-label,'')])")

