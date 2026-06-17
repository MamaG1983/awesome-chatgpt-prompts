from playwright.sync_api import sync_playwright
import subprocess
import time
import os

def run_verification():
    # Start the server
    server_process = subprocess.Popen(
        ["python3", "-m", "http.server", "8080"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    time.sleep(2) # Wait for server to start

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context()

            # Tracking requests
            csv_requests = {
                "prompts.csv": 0,
                "vibeprompts.csv": 0
            }

            def handle_request(request):
                url = request.url
                if "prompts.csv" in url and "vibeprompts.csv" not in url:
                    csv_requests["prompts.csv"] += 1
                    print(f"Request for prompts.csv: {url}")
                elif "vibeprompts.csv" in url:
                    csv_requests["vibeprompts.csv"] += 1
                    print(f"Request for vibeprompts.csv: {url}")

            page = context.new_page()
            page.on("request", handle_request)

            print("Testing Vibe Page (vibe/test_verify.html)...")
            # Navigate directly to vibe test page
            page.goto("http://localhost:8080/vibe/test_verify.html")
            page.wait_for_timeout(3000)

            print("Simulating multiple search keystrokes in Vibe...")
            vibe_search = page.locator("#searchInput")
            vibe_search.fill("R")
            page.wait_for_timeout(200)
            vibe_search.fill("Re")
            page.wait_for_timeout(200)
            vibe_search.fill("Rea")
            page.wait_for_timeout(200)
            vibe_search.fill("React")
            page.wait_for_timeout(500)

            # Verification assertions for Vibe
            # Should be exactly 1 request for vibeprompts.csv despite multiple keystrokes
            print(f"Total vibeprompts.csv requests: {csv_requests['vibeprompts.csv']}")
            assert csv_requests["vibeprompts.csv"] == 1, f"Expected 1 request for vibeprompts.csv, got {csv_requests['vibeprompts.csv']}"

            print("Testing Main Page (test_verify.html)...")
            # Navigate to main test page
            page.goto("http://localhost:8080/test_verify.html")
            page.wait_for_timeout(3000)

            print("Simulating search and filter in Main...")
            search_input = page.locator("#searchInput")
            search_input.fill("A")
            page.wait_for_timeout(200)
            search_input.fill("Ac")
            page.wait_for_timeout(200)
            search_input.fill("Act")
            page.wait_for_timeout(500)

            audience_select = page.locator("#audienceSelect")
            audience_select.select_option("developers")
            page.wait_for_timeout(500)
            audience_select.select_option("everyone")
            page.wait_for_timeout(500)

            # Verification assertions for Main
            # Should be exactly 1 request for prompts.csv on this page load
            # Note: since it's a new page load, it will be +1.
            print(f"Total prompts.csv requests: {csv_requests['prompts.csv']}")
            # If it was 0 before, it should be 1 now.
            assert csv_requests["prompts.csv"] == 1, f"Expected 1 request for prompts.csv on main page load, got {csv_requests['prompts.csv']}"

            print("Verification SUCCESS: CSVs requested only once per page session despite multiple interactions.")

            # Take screenshot for record
            os.makedirs("/home/jules/verification/screenshots", exist_ok=True)
            page.screenshot(path="/home/jules/verification/screenshots/verification_cache.png")

            context.close()
            browser.close()
    finally:
        server_process.terminate()
        server_process.wait()

if __name__ == "__main__":
    run_verification()
