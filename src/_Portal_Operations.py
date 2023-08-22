from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Returns the driver object with the URL of TeduPORTAL.
def get_portal():
    portal_URL = "https://my.tedu.edu.tr/home"
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(portal_URL)
    driver.maximize_window()
    return driver

# Logs in to Portal.
def login(driver, id, pw):
    user_id_path = driver.find_element(By.XPATH, "/html/body/div/div[4]/form/div[1]/div[1]/div/input")
    user_id_path.send_keys(id)
    user_password_path = driver.find_element(By.XPATH, "/html/body/div/div[4]/form/div[1]/div[2]/div/input")
    user_password_path.send_keys(pw)
    login_button = driver.find_element(By.XPATH, "/html/body/div/div[4]/form/div[3]/div[1]/button/span[1]")
    login_button.click()
    time.sleep(5)

def get_courses_offered(driver):
    courses_offered_button = driver.find_element(By.XPATH, "//*[@id='__tile17']")
    courses_offered_button.click()
    time.sleep(10)

# Function to list and extract data.
def list_data(driver, year, semester):

    # Inner functions to create appropriate tables on the site with the desired parameters.
    def semester_chooser():
        driver.find_element(By.XPATH, "//*[@id='WD2C-btn']").click()
        time.sleep(1)
        if semester == "fall":
            driver.find_element(By.XPATH, "//*[@id='WD2E']").click()
            time.sleep(0.5)
        elif semester == "spring":
            driver.find_element(By.XPATH, "//*[@id='WD2F']").click()
            time.sleep(0.5)

    # Clicks on list courses button then waits for table to be loaded.
    def click_list_courses():
        driver.find_element(By.XPATH, "//*[@id='WD57']").click()
        print("clicked list courses at", datetime.now())
        time.sleep(85)

    # Actual function to reveal table.
    def reveal_table(xpath):
        driver.find_element(By.XPATH, "//*[@id='{}']".format(xpath)).click()
        time.sleep(0.5)
        semester_chooser()
        click_list_courses()

    # Courses Offered page opens in a new tab, switching driver's selected tab.
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(0.1)

    # Clicking on year selector button, then doing appropriate operations with respect to parameters.
    driver.find_element(By.XPATH, "//*[@id='WD19-btn']").click()
    time.sleep(0.5)
    
    accepted_years = ["2017/2018", "2018/2019", "2019/2020", "2020/2021", "2021/2022", "2022/2023"]
    
    if year not in accepted_years:
        raise Exception(f"Unexpected year to scrape: {year}. Please modify the configuration file.\nAccepted years: {accepted_years}")

    # Below XPATHs are consecutively grows, can be modified as wanted.
    if year == "2017/2018":
        reveal_table("WD20")
    elif year == "2018/2019":
        reveal_table("WD21")
    elif year == "2019/2020":
        reveal_table("WD22")
    elif year == "2020/2021":
        reveal_table("WD23")
    elif year == "2021/2022":
        reveal_table("WD24")
    elif year == "2022/2023":
        reveal_table("WD25")
        

def extract_data(driver):
    all_data = {}
    courses_list = []
    lecturers_list = []
    number_of_students_list = []
    number_of_unsuccessful_students_list = []
    gpas_list = []

    print("Loops started at", datetime.now())
    # Courses
    for i in driver.find_elements(By.XPATH, "//td[@cc='0']"):
        courses_list.append(i.text)
    # print("Courses done at", datetime.now())
    # Lecturers
    for i in driver.find_elements(By.XPATH, "//td[@cc='10']"):
        lecturers_list.append(i.text[:-1])
    # print("Lecturers done at", datetime.now())

    # Number of students took the course
    for i in driver.find_elements(By.XPATH, "//td[@cc='13']"):
        number_of_students_list.append(i.text.replace(" ", ""))
    # print("# of students done at", datetime.now())

    # Number of unsuccessful students
    for i in driver.find_elements(By.XPATH, "//td[@cc='15']"):
        number_of_unsuccessful_students_list.append(i.text.replace(" ", ""))
    # print("# of unsuccessful students done at", datetime.now())

    # Gpas
    for i in driver.find_elements(By.XPATH, "//td[@cc='18']"):
        gpas_list.append(i.text.replace(" ", ""))
    # print("Gpas done at", datetime.now())
    print("Loops finished at ", datetime.now())

    a = 0
    for i in courses_list:
        all_data[a+1] = [i, lecturers_list[a], number_of_students_list[a],
                           number_of_unsuccessful_students_list[a], gpas_list[a]]
        a = a + 1
    return all_data


def list_and_extract(driver, year, semester):
    list_data(driver, year, semester)
    return extract_data(driver)
