import _Portal_Operations as Portal
import _Database_Operations as Database
import json


if __name__ == '__main__':
    config_file = open("config.json")
    configs = json.load(config_file)
    use_database = configs["use_database"]
    
    if use_database:
        Database.table_controller()

    # Necessary information to log into Portal.
    PORTAL_ID = input("PORTAL ID: ")
    PORTAL_PW = input("PORTAL PW: ")

    print("\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n\n")
    print("\nProcess began at {}\n".format(Portal.datetime.now()))

    driver = Portal.get_portal()
    Portal.login(driver, PORTAL_ID, PORTAL_PW)
    Portal.get_courses_offered(driver)

    def extract_and_insert(driver_var, year, semester):
        dictionary = Portal.list_and_extract(driver_var, year, semester)
        if use_database: 
            Database.insert_to_lectures(year + " " + semester.capitalize(), dictionary)
        print(dictionary)
        print("Data of", year + " " + semester.capitalize(), "has been scraped.\n")
        
    years_to_scrape = configs["years_to_scrape"]

    for year in years_to_scrape:
        extract_and_insert(driver, year, "fall")
        extract_and_insert(driver, year, "spring")

    print("Process finished at", Portal.datetime.now())

    driver.close()