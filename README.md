# SCBRS
---

# Selenium CAPTCHA Bypass Results Scraper 🚀

![Banner](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExazE2aGJybnJzdnN6dXIzbjJmdWF5MDl2bWFuc2ZxZm05ZjFwbmExNyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/CILGGl6sizxVC/giphy.gif)

Welcome to the **Selenium CAPTCHA Bypass Results Scraper**! This repository contains a Python project that uses [undetected-chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver) and [selenium-stealth](https://github.com/diprajpatra/selenium-stealth) to scrape Google search results while minimizing detection. If a CAPTCHA appears, the script pauses so you can solve it manually — a completely free solution! 🙌

## Features ✨

- **Automated Google Search Scraping:** Extracts search result titles from Google.
- **Manual CAPTCHA Bypass:** Detects CAPTCHA, saves a screenshot, and pauses for manual resolution.
- **Human-like Interaction:** Introduces random delays to mimic natural browsing.
- **Stealth Mode:** Uses undetected-chromedriver and selenium-stealth to mimic a real browser fingerprint.
- **Error Handling:** Robust try/except blocks ensure the script continues if issues occur.
- **Cross-Platform Commands:** Detailed instructions for Windows, macOS, and Linux users.

## Setup & Installation 🛠️

### 1. Clone the Repository

```bash
git clone https://github.com/riyann00b/SCBRS.git
cd SCBRS
```

### 2. Create and Activate a Virtual Environment

#### Windows (CMD or PowerShell):

```cmd
python -m venv venv
venv\Scripts\activate
```

#### macOS/Linux (Bash):

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

All required libraries are listed in the `requirements.txt` file. Install them with:

```bash
pip install -r requirements.txt
```

Your `requirements.txt` should include:

```txt
selenium
undetected-chromedriver
selenium-stealth
requests
```

### 4. Download the ChromeDriver 🔽

Visit [Chrome for Testing](https://googlechromelabs.github.io/chrome-for-testing/) to download the correct ChromeDriver binary.  
> **Note:** You do **not** need to manually check your Chrome version; simply follow the link above and download the appropriate driver for your system.  
> Once downloaded, extract the binary and either add it to your system’s PATH or note its location for later use.

### 5. (Optional) Check Your Google Chrome Version 🖥️

If you wish to verify your Chrome version:

#### Windows (CMD):

```cmd
reg query "HKEY_CURRENT_USER\Software\Google\Chrome\BLBeacon" /v version
```

#### macOS:

```bash
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --version
```

#### Linux:

```bash
google-chrome --version
```

## Usage 🚀

Run the main Python script:

```bash
python main.py
```

The script will:
1. Launch an undetected Chrome instance with realistic browser fingerprints.
2. Navigate to a Google search URL (e.g., `https://www.google.com/search?q=Selenium+captcha+test`).
3. To mimic human behavior, Wait for a few seconds (with randomized delays).
4. **Check for CAPTCHA:**  
   - If a CAPTCHA is detected, it saves a screenshot (`captcha.png`) and pauses for manual intervention.
5. Scrape the search results (titles) and print them.
6. Save the extracted titles to a text file called `results.txt`.

## How It Works 🔍

### Browser Automation & Stealth

- **Undetected Chromedriver:**  
  Launches a Chrome instance that minimizes automation detection.
  
- **Selenium Stealth:**  
  Applies stealth configurations (custom user agent, language, vendor, platform, etc.) so your automated browser mimics a real user's fingerprint.

### CAPTCHA Handling

- **Detection & Manual Bypass:**  
  The script uses explicit waits to detect if a CAPTCHA iframe is present. If found, it saves a screenshot and pauses, prompting you to solve the CAPTCHA manually. Once solved, press Enter to continue.

### Human-like Behavior

- **Randomized Delays:**  
  Uses `time.sleep()` with random intervals to simulate natural human interaction, reducing the risk of CAPTCHA triggers.

### Scraping & Data Storage

- **Scraping Logic:**  
  After (and if) the CAPTCHA is solved, the script locates search result blocks (using the selector `"div.g"`) and extracts text from `<h3>` tags.
- **Saving to File:**  
  Extracted titles are saved in a formatted manner into `results.txt`.

## Code Overview 💻

Below is a simplified view of key sections of the code:

- **Initialization & Stealth Setup:**

  ```python
  options = uc.ChromeOptions()
  # For manual CAPTCHA solving, run in non-headless mode:
  # options.add_argument("--headless")
  options.add_argument("--no-sandbox")
  options.add_argument("--disable-dev-shm-usage")
  driver = uc.Chrome(options=options)
  
  stealth(
      driver,
      user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)...",
      languages=["en-US", "en"],
      vendor="Google Inc.",
      platform="Win32",
      webgl_vendor="Intel Inc.",
      renderer="Intel Iris OpenGL Engine",
      fix_hairline=True,
  )
  ```

- **Manual CAPTCHA Check:**

  ```python
  def wait_for_manual_captcha_resolution(driver, timeout=120):
      try:
          captcha_iframe = WebDriverWait(driver, 10).until(
              EC.presence_of_element_located((By.XPATH, "//iframe[contains(@src, 'recaptcha')]"))
          )
          print("CAPTCHA detected! Please solve it manually in the browser.")
          driver.save_screenshot("captcha.png")
          input("After solving the CAPTCHA, press Enter to continue...")
      except Exception as e:
          print("No CAPTCHA detected (or error during CAPTCHA check):", e)
  ```

- **Scraping & Saving Results:**

  ```python
  result_elements = driver.find_elements(By.CSS_SELECTOR, "div.g")
  results = []
  for element in result_elements:
      try:
          title = element.find_element(By.TAG_NAME, "h3").text.strip()
          if title:
              results.append(title)
      except Exception:
          continue
  
  with open("results.txt", "w", encoding="utf-8") as f:
      for idx, title in enumerate(results, start=1):
          f.write(f"Result {idx}:\nTitle: {title}\n{'-'*50}\n")
  ```

## Contributing 🤝

Contributions, bug reports, and feature requests are very welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## License 📄

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

## Final Notes ✨

> **⚠️ Warning:**  
> Bypassing CAPTCHA—even for scraping purposes—may violate the target website’s terms of service. This project is intended for educational and testing purposes only. Use responsibly!

Happy Scraping! 😄👍
