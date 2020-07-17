# Import the Python standard libraries needed to run the code
import os
import random

# Import the third-party libraries needed to run the code
from PIL import Image, ImageFilter
import requests
from twython import Twython

# Pass the environment variables into Twython to be used to authenticate into Twitter and tweet
twitter = Twython(
    os.environ.get("APP_KEY"),
    os.environ.get("APP_SECRET"),
    os.environ.get("OAUTH_TOKEN"),
    os.environ.get("OAUTH_TOKEN_SECRET"),
)


def main():
    # Create the URL for the image (Unsplash returns a random image) and set the image download path
    file_url = "https://source.unsplash.com/collection/461104/1/"
    file_path = "1.jpg"

    # If for some unknown reason, the file already exists, skip the next step
    if os.path.exists(file_path):
        pass
    # If the file does not exist, use the Requests library to download and close the file
    else:
        response = requests.get(file_url)
        file = open(file_path, "wb")
        file.write(response.content)
        file.close()

    # Open the image using the Pillow library
    new_image = Image.open(file_path)

    # Show the image before the transformation
    new_image.show()

    # Call the "Negative" Algorithm to apply it to the image as an image filter
    negative_algorithm(new_image, file_path)

    # Open the modified image
    modified_image = open(file_path, "rb")

    # Use Twython library to upload and tweet the modified image, optionally with a `status` message
    response = twitter.upload_media(
        media=modified_image, media_type="image", media_category="tweet_image"
    )
    twitter.update_status(status="", media_ids=[response["media_id"]])

    # Call the `remove_file()` function to delete the image
    remove_file(file_path)


# Apply the "Negative" Algorithm
def negative_algorithm(new_image, file_path):

    width, height = new_image.size
    negative_image = Image.new("RGB", (width, height))
    raw_pixels = new_image.load()
    negative_pixels = negative_image.load()

    for y in range(height):
        for x in range(width):
            R, G, B = raw_pixels[x, y]
            oR = (R * 0.393) + (G * 0.769) + (B * 0.189)
            oG = (R * 0.349) + (G * 0.686) + (B * 0.168)
            oB = (R * 0.272) + (G * 0.534) + (B * 0.131)
            negative_pixels[x, y] = (255 - R, 255 - G, 255 - B)

    modified_image = negative_image
    save_image(modified_image, file_path)


# Save modified image and return; optionally, show the image after the transformation
def save_image(modified_image, file_path):
    modified_image.show()
    modified_image.save(file_path)
    return modified_image


# If file exists, remove file
def remove_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)


if __name__ == "__main__":
    main()
