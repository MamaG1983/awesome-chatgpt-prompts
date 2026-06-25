import asyncio
import subprocess
import time
from playwright.async_api import async_playwright

async def verify_fetches():
    # Start local server
    server = subprocess.Popen(["python3", "-m", "http.server", "8000"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(2)  # Give server time to start

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Track CSV requests
        csv_requests = []
        page.on("request", lambda request: csv_requests.append(request.url) if request.url.endswith(".csv") else None)

        print("--- Testing /vibe/ ---")
        await page.goto("http://localhost:8000/vibe/test_verify.html")
        await page.wait_for_selector("#searchInput")

        # Initial load might fetch once or twice depending on implementation
        initial_fetches = len([r for r in csv_requests if "vibeprompts.csv" in r])
        print(f"Initial fetches for vibeprompts.csv: {initial_fetches}")

        # Type something to trigger search fetches
        await page.fill("#searchInput", "test")
        await asyncio.sleep(1)

        total_fetches_vibe = len([r for r in csv_requests if "vibeprompts.csv" in r])
        print(f"Total fetches for vibeprompts.csv after typing 'test': {total_fetches_vibe}")

        if total_fetches_vibe > initial_fetches:
            print("Confirmed: Redundant fetches on keystroke in /vibe/")

        # Clear requests for next test
        csv_requests.clear()

        print("\n--- Testing root / ---")
        await page.goto("http://localhost:8000/test_verify.html")
        await page.wait_for_selector("#searchInput")

        initial_fetches_main = len([r for r in csv_requests if "prompts.csv" in r])
        print(f"Initial fetches for prompts.csv: {initial_fetches_main}")

        # Trigger audience change which calls filterPrompts()
        if await page.query_selector("#audienceSelect"):
            await page.select_option("#audienceSelect", "developers")
            await asyncio.sleep(1)

            total_fetches_main = len([r for r in csv_requests if "prompts.csv" in r])
            print(f"Total fetches for prompts.csv after audience change: {total_fetches_main}")

            if total_fetches_main > initial_fetches_main:
                print("Confirmed: Redundant fetch on audience change in /")

        await browser.close()

    server.terminate()

if __name__ == "__main__":
    asyncio.run(verify_fetches())
