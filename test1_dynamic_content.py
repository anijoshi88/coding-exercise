from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


# Returns the dynamic text content from the page
# Uses top level CSS selector that includes all the rows of text
def read_content(driver, page):

    driver.get(page)
    dynamic_text_block = driver.find_element(By.CSS_SELECTOR, "div.large-10.columns.large-centered")

    return dynamic_text_block.text


def cleanup(driver):
    # close the Selenium driver
    driver.quit()


# Tests that the dynamic text on the page contains a word at least "expected_length" characters in length
def test1(dynamic_text_block, expected_length):

    words = dynamic_text_block.split()
    word_found = False

    # Finds the first word that is at least "expected_length"
    for word in words:
        if len(word) >= expected_length:
            word_found = True
            break

    assert word_found == True, "Word with at least %d characters not found" %expected_length


# Finds the longest word on the page and prints it
# If multiple words with same longest length are present, prints the last one
def find_longest_word(dynamic_text_block):
    words = dynamic_text_block.split()
    length_of_longest_word = 0
    longest_word_found = ""

    for word in words:
        if len(word) > length_of_longest_word:
            # If longest word is at end of sentence, strip the period
            longest_word_found = word.strip(".")
            length_of_longest_word = len(longest_word_found)

    print("Longest word on the page is %s and is %d characters long" % (longest_word_found, length_of_longest_word))


if __name__ == '__main__':
    # Initialize selenium driver
    s = Service(ChromeDriverManager().install())
    chrome_driver = webdriver.Chrome(service=s)
    chrome_driver.maximize_window()

    page_under_test = 'https://the-internet.herokuapp.com/dynamic_content'

    dynamic_text = read_content(chrome_driver, page_under_test)
    exp_length = 10

    try:
        assert dynamic_text, "Text block is empty"
        # Stretch goal - Prints longest word first everytime (since test1 might fail)
        find_longest_word(dynamic_text)
        test1(dynamic_text, exp_length)
    except AssertionError as error:
        print(error)
    finally:
        cleanup(chrome_driver)
