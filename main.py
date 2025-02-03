#!/usr/bin/env python3
import time
import random
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_stealth import stealth


def wait_for_manual_captcha_resolution(driver, timeout=120):
    """
    If a CAPTCHA iframe is detected, save a screenshot and pause execution
    so you can solve the CAPTCHA manually. Waits up to 10 seconds for the CAPTCHA
    iframe to appear.
    """
    try:
        captcha_iframe = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//iframe[contains(@src, 'recaptcha')]"))
        )
        print("CAPTCHA detected! Please solve it manually in the browser.")
        driver.save_screenshot("captcha.png")
        print("A screenshot has been saved as 'captcha.png'.")
        input("After solving the CAPTCHA, press Enter to continue...")
    except Exception as e:
        print("No CAPTCHA detected (or error during CAPTCHA check):", e)


def save_results_to_file(results, filename="results.txt"):
    """
    Saves the list of result titles to a text file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        for idx, title in enumerate(results, start=1):
            f.write(f"Result {idx}:\n")
            f.write(f"Title: {title}\n")
            f.write("-" * 50 + "\n")
    print(f"Results saved to {filename}")


def main():
    # Configure undetected Chromedriver options.
    options = uc.ChromeOptions()
    # For manual CAPTCHA solving, it's best to run without headless mode.
    # Uncomment the next line if you want a headless browser.
    # options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Initialize the undetected Chrome driver.
    driver = uc.Chrome(options=options)

    # Use Selenium Stealth to make the browser fingerprint more humanlike.
    stealth(
        driver,
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
    )

    try:
        # Open a Google search URL.
        target_url = "https://www.google.com/search?q=Selenium+captcha+test"
        driver.get(target_url)
        # Randomized delay to mimic human behavior.
        time.sleep(3 + random.uniform(0, 2))

        # Check for a CAPTCHA and wait for manual solving if present.
        wait_for_manual_captcha_resolution(driver)

        # Scrape result elements (using a common selector; note that Google’s HTML changes over time).
        result_elements = driver.find_elements(By.CSS_SELECTOR, "div.g")
        results = []
        for element in result_elements:
            try:
                title = element.find_element(By.TAG_NAME, "h3").text.strip()
                if title:
                    results.append(title)
            except Exception:
                continue

        if not results:
            print("No results found.")
        else:
            print(f"Found {len(results)} results.")
            # Save results to a text file.
            save_results_to_file(results, "results.txt")
    except Exception as ex:
        print("An error occurred during scraping:", ex)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()