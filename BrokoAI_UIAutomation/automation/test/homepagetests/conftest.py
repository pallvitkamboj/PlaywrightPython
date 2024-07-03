import pytest
import tkinter
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="module")
def set_up(playwright: sync_playwright()):
    global browser, context, page
    try:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(
            geolocation={"longitude": 45.158853, "latitude": -77.993517}, permissions=["geolocation"])
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = context.new_page()
        screen = tkinter.Tk()
        page.set_viewport_size({"width": screen.winfo_screenwidth() - 10, "height": screen.winfo_screenheight() - 10})
        page.goto("https://www.broko.ai/")
        yield page
    except Exception as e:
        print("Failed to initialize browser successfully " + str(e))
    finally:
        context.tracing.stop(path="trace.zip")
        context.close()
        browser.close()
