import sys
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# default path to file to store data
path_to_file = ("D://Documents//Archaeology//Projects//AH_Sentiment//ah_scrapes//ahscrape.csv")

# default number of scraped pages
num_page = 2

# default tripadvisor website of hotel or things to do (attraction/monument) 
url = "https://www.tripadvisor.com/Attraction_Review-g844595-d7733923-Reviews-Heraion_of_Argos-Argos_Argolis_Region_Peloponnese.html"
#url = "https://www.tripadvisor.com/Attraction_Review-g844595-d7733923-Reviews-Heraion_of_Argos-Argos_Argolis_Region_Peloponnese.html"

# if you pass the inputs in the command line
if (len(sys.argv) == 4):
    path_to_file = sys.argv[1]
    num_page = int(sys.argv[2])
    url = sys.argv[3]

# import the webdriver and direct Python/Selenium to filepath
driver = webdriver.Chrome("C://Users//nsusm//AppData//Local//Programs//Python//Python39//webdriver//bin//chromedriver.exe")

# direct driver to the html of your review
driver.get('https://www.tripadvisor.com/Attraction_Review-g844595-d7733923-Reviews-Heraion_of_Argos-Argos_Argolis_Region_Peloponnese.html')


# open the file to save the review
csvFile = open(path_to_file, 'w', newline='')
csvFile = open(path_to_file, 'w', encoding="utf-8", newline='')
csvWriter = csv.writer(csvFile, newline='', delimiter=',')
csvWriter.writerow([str ('person'), str ('title'), str ('rating'), str ('review'), str ('review_date')])

# change the value inside the range to save more or less reviews (# start, #end, #interval)
for i in range(0, 50, 1):

    # expand the review (how many seconds to let page load)
    time.sleep(5)

# define container/where on the webpage to direct the search. This is like an html filepath. On the TA website, this is the individual box for each person's review
    container = driver.find_elements_by_xpath(".//div[@class='review-container']")

# define what datasets to find: name = [container from above].[search tool].[xpath name].[additional commands]   
    for j in range(len(container)):
        rating = container[j].find_element_by_xpath(".//div[contains(@class, 'jVDab o W f u w GOdjs')]").get_attribute("aria-label").split("_")[3]
        person = container[j].find_element_by_class_name('BMQDV _F G- wSSLS SwZTJ FGwzt ukgoS').text.split("\n")[0]#person but not place
        title = container[j].find_element_by_class_name('yCeTE').text.split("\n")("\n", "  ")
        review = container[j].find_element_by_xpath(".//div[contains[@class, 'biGQs _P pZUbB KxBGd')]").text.replace("\n", "  ")
        review_date = container[j].find_element_by_class_name('RpeCd').text
                                                  
#write data into your csv
        csvWriter.writerow([person, title, rating, review, review_date])
        
# change the page            
    driver.find_element(By.XPATH, "//a[@class='BrOJk u j z _F wSSLS tIqAi unMkR']").click()   

#quit selenium
driver.quit()

print ("complete")
                                                  
#FYI you need to close all windows for the file to write

