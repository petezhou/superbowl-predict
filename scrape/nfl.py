import sys
import requests
from bs4 import BeautifulSoup
import csv 
from pprint import pprint
from selenium import webdriver
import time

def main():

    with open("winner.txt") as f:
        content = f.readlines()
    content = [x.strip() for x in content] 
 
    for i in range(2017, 1976, -1):
        read_page(i, content[-(i - 2017)])



def read_page(year, winner):
    #print(str(year))

    #get defensive stats
    url = 'https://www.pro-football-reference.com/years/' + str(year) + '/opp.htm'
    req = requests.get(url)
    html_doc = req.text
    soup1 = BeautifulSoup(html_doc, "html.parser")
    #get offensive stats
    driver = webdriver.Chrome()
    url = 'https://www.pro-football-reference.com/years/' + str(year) + '/'
    driver.maximize_window()
    driver.get(url)
    time.sleep(5)
    content = driver.page_source.encode('utf-8').strip()
    soup2 = BeautifulSoup(content, "html.parser")

    defensive = soup1.find("div", id="div_team_stats").find("tbody").find_all("tr")
    offensive = soup2.find("div", id="div_team_stats").find("tbody").find_all("tr")


    for team in defensive:
        name = team.find("a").text
        points_allowed = team.find("td", attrs={"data-stat":"points"}).text
        
        points_scored = ""
        for off_team in offensive:
            if name == off_team.find("a").text:
                points_scored = off_team.find("td", attrs={"data-stat":"points"}).text
                break

        isSuperbowl = 0
        if name == winner:
            isSuperbowl = 1

        print(points_scored + "," + points_allowed + "," +  str(isSuperbowl))



if __name__ == '__main__':
	main()
