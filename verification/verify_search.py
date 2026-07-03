from playwright.sync_api import sync_playwright
import os

def run_verification(page):
    # 1. Test Main Page Search
    page.goto("http://localhost:8080/")
    page.wait_for_selector("#searchInput")
    page.wait_for_timeout(1000)

    # Search for "Linux"
    page.fill("#searchInput", "Linux")
    page.wait_for_timeout(1000)

    # Verify search results appear
    page.wait_for_selector("#searchResults .search-result-item")
    page.wait_for_timeout(1000)

    # Take screenshot of main page search
    page.screenshot(path="verification/screenshots/main_search.png")

    # 2. Test Vibe Page Search
    page.goto("http://localhost:8080/vibe/")
    page.wait_for_selector("#searchInput")
    page.wait_for_timeout(1000)

    # Search for "React"
    page.fill("#searchInput", "React")
    page.wait_for_timeout(1000)

    # Verify search results appear
    page.wait_for_selector("#searchResults .search-result-item")
    page.wait_for_timeout(1000)

    # Take screenshot of vibe page search
    page.screenshot(path="verification/screenshots/vibe_search.png")

    # Final state
    page.wait_for_timeout(1000)

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            record_video_dir="verification/videos"
        )
        page = context.new_page()
        try:
            run_verification(page)
        finally:
            context.close()
            browser.close()
