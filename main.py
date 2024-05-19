from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.config import Config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
import requests

# Set window size and resolution
Window.size = (400, 300)
Config.set('graphics', 'resizable', False)

class InstagramDownloader(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Logo
        logo = Image(source='images/logo.png')  # Replace 'logo.png' with your logo file path
        layout.add_widget(logo)

        # Title label
        title_label = Label(text='Instagram Downloader', font_size=24, bold=True, color=(0, 0.7, 0.9, 1))
        layout.add_widget(title_label)

        # Text input field
        self.input_field = TextInput(hint_text='Enter Instagram reel link', multiline=False, size_hint=(1, None), height=40,
                                     background_color=(0.95, 0.95, 0.95, 1), font_size=16)
        layout.add_widget(self.input_field)

        # Download button
        download_button = Button(text='Download Content', size_hint=(1, None), height=40, background_color=(0, 0.7, 0.9, 1))
        download_button.bind(on_press=self.download_content)
        layout.add_widget(download_button)

        # Result label
        self.result_label = Label(text='Mithun Dev', font_size=14, color=(0.5, 0.5, 0.5, 1))
        layout.add_widget(self.result_label)

        return layout

    def extract_content_url(self):
        url = self.input_field.text

        # Validate URL
        if not url.startswith('https://www.instagram.com/reel/'):
            return 'Error: Invalid Instagram reel link'

        # Configure Selenium options
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run Chrome in headless mode
        chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
        driver = webdriver.Chrome(options=chrome_options)

        try:
            # Open the Instagram reel URL in the browser
            driver.get(url)

            # Find the script tag containing the content URL
            find = driver.find_element(by=By.XPATH, value='/html/head/script[3]')
            text = find.get_attribute('innerText')

            # Extract the content URL from the script
            start = text.index('"contentUrl":"')
            end = text.index('","thumbnailUrl"', start + 14)
            content_url = text[start + 14:end].replace('\/', '/')

            return content_url
        except Exception as e:
            return f'Error: {e}'
        finally:
            # Close the WebDriver
            driver.quit()

    def download_content(self, instance):
        content_url = self.extract_content_url()  # Call extract_content_url to get the URL
        if content_url.startswith('http'):
            # Get the filename from the URL
            filename = os.path.basename(content_url)

            try:
                # Create the directory if it doesn't exist
                save_folder = os.path.join(os.path.expanduser('~'), 'Insup')
                os.makedirs(save_folder, exist_ok=True)

                # Save the content to a file in the specific folder
                save_path = os.path.join(save_folder, filename)
                with open(save_path, 'wb') as f:
                    response = requests.get(content_url, stream=True)
                    for chunk in response.iter_content(chunk_size=1024):
                        if chunk:
                            f.write(chunk)

                self.result_label.text = f'Downloaded video saved as: {save_path}'
            except Exception as e:
                self.result_label.text = f'Error downloading content: {e}'
        else:
            self.result_label.text = content_url


if __name__ == '__main__':
    InstagramDownloader().run(
