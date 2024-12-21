#youtube automation
from selenium import webdriver

class Music():
            try:
            self.query = query
            self.driver.get("https://www.youtube.com/results?search_query=" + self.query)
    
            # Find the first video and click it
            video = self.driver.find_element(
                By.XPATH, '//*[@id="dismissible"]')
            video.click()

            # Try skipping ads if present
            try:
                # Find and click the "Skip Ad" button (it may be invisible initially, so use a wait time)
                skip_button = self.driver.find_element(
                    By.XPATH, '//*[@class="ytp-ad-skip-button ytp-button"]')
                skip_button.click()
                print("Ad skipped!")
            except:
                print("No ad or unable to skip.")

        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            # Keeps the browser open until you press a key
            input("Press any key to exit...")
