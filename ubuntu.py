import os
import requests
from urllib.parse import urlparse

def fetch_image():
    # Ask user for the image URL
    url = input("Enter the URL of the image you want to fetch: ").strip()

    # Directory for fetched images
    folder = "Fetched_Images"
    os.makedirs(folder, exist_ok=True)  # Respect: Create if it doesn’t exist

    try:
        # Try fetching the image
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Will raise an error for bad HTTP responses

        # Extract filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        # If no filename found, generate one
        if not filename:
            filename = "downloaded_image.jpg"

        filepath = os.path.join(folder, filename)

        # Save the image in binary mode
        with open(filepath, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)

        print(f"✅ Image successfully saved as {filepath}")

    except requests.exceptions.HTTPError as e:
        print(f"⚠️ HTTP Error: {e}")
    except requests.exceptions.ConnectionError:
        print("⚠️ Connection error. Please check your internet connection.")
    except requests.exceptions.Timeout:
        print("⚠️ The request timed out. Try again later.")
    except Exception as e:
        print(f"⚠️ An error occurred: {e}")

if __name__ == "__main__":
    fetch_image()
