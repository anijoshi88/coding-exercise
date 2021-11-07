from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


# Returns all elements in the page with img tag
def get_list_of_images(driver, page_under_test):
    driver.get(page_under_test)
    list_of_images = driver.find_elements(By.TAG_NAME, "img")
    return list_of_images


# Extracts the avatar names from img url and prints them
def print_avatar_names(list_of_images):
    avatar_names = []

    # Loop through the list of images...
    # and extract the ones that contain "Avatar" in src tag
    for image in list_of_images:
        url = image.get_attribute("src")

        # If src url contains "Avatar", slice the name from it
        if "Avatar" in url:
            avatar_names.append(url[-12:-4])

    print("\nAvatar names that appear on the page: ")
    for avatar in avatar_names:
        print(avatar)


# Tests if punisher image exists on the page. Fails the test if it does
def test_punisher_image_exists():
    # Initialize selenium driver
    s = Service(ChromeDriverManager().install())
    chrome_driver = webdriver.Chrome(service=s)
    chrome_driver.maximize_window()

    page_under_test = 'https://the-internet.herokuapp.com/dynamic_content'
    punisher_image = 'Original-Facebook-Geek-Profile-Avatar-3.jpg'
    list_of_images = get_list_of_images(chrome_driver, page_under_test)

    punisher_image_found = False
    for image in list_of_images:
        src_link = image.get_attribute("src")
        if punisher_image in src_link:
            punisher_image_found = True

    # Stretch goal - Print all avatar names that appear on the page
    print_avatar_names(list_of_images)

    try:
        assert punisher_image_found == False, "Punisher image appears on the page"
    finally:
        chrome_driver.quit()



