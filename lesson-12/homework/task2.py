import requests
import sqlite3
import csv
from bs4 import BeautifulSoup
connection = sqlite3.connect("Jobs.db")
cursor = connection.cursor()
cursor.execute("""
        CREATE TABLE Jobs(
            job_title TEXT UNIQUE
            company TEXT UNIQUE
            location TEXT UNIQUE
            job_description TEXT
            application_link TEXT
        )
""")


response = requests.get("https://realpython.github.io/fake-jobs")
soup = BeautifulSoup(response.text,'html.parser')
cards = soup.find_all("div",class_="card-content")
for card in cards:
    links = card.find_all("a", class_="card-footer-item")
    if len(card)>1:
        job_title = "Job title: ",card.get_text("h2")
        company = "Company: ",card.get_text("h3")
        location ="Location: ",card.get_text("p",class_="location")
        job_description ="Job description: ",links[0].get("href")
        application_link ="Application link: ",links[1].get("href")
        data = (job_title, company, location, job_description, application_link)
        cursor.execute("INSERT INTO Jobs(job_title,company,location,job_description,application_link) VALUES(?,?,?,?,?) ON DUPLICATE KEY UPDATE job_description = VALUES(job_description), application_link = VALUES(application_link)")
        connection.commit()
def filter(company_name):
    with open("file.csv","w",newline="") as file:
        cursor.execute("SELECT * FROM Jobs WHERE company_name=?",(company_name))
        elements = cursor.fetchall()
        writer = csv.writer(file)
        writer.writerow("Job title","Company","Location","Job description","Application link")
        for element in elements:
            writer.writerow(element)