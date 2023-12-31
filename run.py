from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from undetected_chromedriver import Chrome, ChromeOptions
import time

options = ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = Chrome(options=options, executable_path=ChromeDriverManager().install())
driver.maximize_window()

Element_Names = []
Element_Phones = []
Cayman_Bracs = []
FirstNames = []
LastNames = []
Boxs = []
Address_lines = []
KY_Numbers = []
Islands = []

basicurl = "https://cayman.directory/en/search/people/a/Cayman-Brac/sortby/relevance/page/"

for i in range(1, 35):
    pageURL = basicurl + str(i)
    # print(pageURL)
    driver.get(pageURL)
    time.sleep(4)

    Element_Name_box = driver.find_elements(By.CLASS_NAME, "h2-list")
    for j in range(len(Element_Name_box)):
        Element_Name = Element_Name_box[j].find_element(By.TAG_NAME, "span").text
        Element_Names = Element_Name.split(" ")
        FirstName = Element_Names[0]
        FirstNames.append(FirstName)
        print("FirstName--> ", FirstName)
        LastName = Element_Names[1]
        LastNames.append(LastName)
        print("LastName--> ", LastName)
    # print(len(Element_Names))

    Element_Phone_box = driver.find_elements(By.CLASS_NAME, "ci-pb")
    for j in range(len(Element_Phone_box)):
        if (j % 2 == 1):
            Element_Phone = Element_Phone_box[j].find_element(By.TAG_NAME, "a").text
            Element_Phones.append(Element_Phone)
    # print(len(Element_Phones))

    Cayman_Brac_box = driver.find_elements(By.CLASS_NAME, "ladd")    
    for j in range(len(Cayman_Brac_box)):
        sentense = Cayman_Brac_box[j].find_element(By.TAG_NAME, "p").text

        sentense_elements = sentense.split(" ")
        if ("Box" in sentense):
            Box = "Box " + sentense_elements[1]
            
            print("Box--> ", Box)
            sentense = sentense.replace(Box, "")
        else :
            Box = " "

        sub_elements = sentense.split("Cayman Brac")
        if (len(sub_elements) == 2):
            Address_line = sub_elements[0]
            print("Address_line--> ", Address_line)
            KY_Number = sub_elements[1]
            print("KY_Number--> ", KY_Number)
        else :
            Address_line = sub_elements[0]
            print("Address_line--> ", Address_line)
            KY_Number = " "

        if ("Cayman Brac" in sentense):
            Island = "Cayman Brac"
        else :
            Island = " "


        Boxs.append(Box)
        Address_lines.append(Address_line)
        KY_Numbers.append(KY_Number)
        Islands.append(Island)




        # Cayman_Bracs.append(Cayman_Brac)
    # print(len(Cayman_Bracs))

    dict = {'First Name': FirstNames, 'Last Name': LastNames, 'BOX #': Boxs, 'Address line 1': Address_lines, 'KY Number': KY_Numbers, 'Island': Islands, 'Phone +1': Element_Phones}
    df = pd.DataFrame(dict)

    df.to_csv('Result.csv', index = False)
