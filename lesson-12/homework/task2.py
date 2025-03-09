import requests
import sqlite3
import csv
from bs4 import BeautifulSoup

# Database setup
db_name = "jobs.db"
conn = sqlite3.connect(db_name)
c = conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS jobs (
        job_title TEXT,
        company TEXT,
        location TEXT,
        description TEXT,
        application_link TEXT,
        PRIMARY KEY (job_title, company, location)
    )
''')
conn.commit()

# Function to scrape job listings
def scrape_jobs():
    url = "https://realpython.github.io/fake-jobs"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    jobs = []
    
    for job in soup.find_all('div', class_='card-content'):
        title = job.find('h2', class_='title').text.strip()
        company = job.find('h3', class_='company').text.strip()
        location = job.find('p', class_='location').text.strip()
        description = job.find('div', class_='description').text.strip()
        application_link = job.find('a', class_='apply')['href']
        
        jobs.append((title, company, location, description, application_link))
    
    return jobs

# Function to insert or update jobs
def store_jobs(jobs):
    for job in jobs:
        c.execute('''
            INSERT INTO jobs (job_title, company, location, description, application_link)
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(job_title, company, location) 
            DO UPDATE SET description=excluded.description, application_link=excluded.application_link
        ''', job)
    conn.commit()

# Function to filter and export jobs
def export_jobs(filter_by=None, value=None, filename='filtered_jobs.csv'):
    query = "SELECT * FROM jobs"
    params = ()
    
    if filter_by in ['company', 'location']:
        query += f" WHERE {filter_by} = ?"
        params = (value,)
    
    c.execute(query, params)
    jobs = c.fetchall()
    
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Job Title", "Company", "Location", "Description", "Application Link"])
        writer.writerows(jobs)
    
    print(f"Filtered jobs exported to {filename}")

# Running the scraper and storing results
jobs = scrape_jobs()
store_jobs(jobs)

# Example Usage
# export_jobs(filter_by='location', value='Remote')
