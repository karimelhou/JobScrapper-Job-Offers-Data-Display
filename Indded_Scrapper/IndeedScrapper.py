from scrapfly import ScrapflyClient, ScrapeConfig
from bs4 import BeautifulSoup
from variables import job_titleS, company_nameS, locationS, salaryS , dateS
import re
from datetime import date, timedelta
import time
from datetime import datetime

client = ScrapflyClient(key="scp-live-b502c4710cb34023a6e50ceeb3a3cae3")

def get_url(job, location):
    template =  "https://www.indeed.com/jobs?q={}&l={}"
    url = template.format(job, location)
    return url
# List of computer science job titles
computer_science_jobs = ['software+engineer', 'data+scientist', 'web+developer', 'cybersecurity+analyst', 'machine+learning+engineer']
while True:
    url = get_url( 'data+scientist', 'United+States')

    result  = client.scrape(ScrapeConfig(
        url= url,
        render_js=True,
        asp=True
    ))



    soup = BeautifulSoup(result.content, 'html.parser')
    job_containers = soup.find_all('div', class_='job_seen_beacon')
    jobs = []  # List to store the job data
    if job_containers:
        for job_seen_beacon in job_containers:
            try:
                job_title_element = job_seen_beacon.find('span', title=True)
                job_title_value = job_title_element['title'] if job_title_element else "Job title not found"
            except AttributeError:
                job_title_value = "Job title not found"

            try:
                company_name_value = job_seen_beacon.find('span', class_='companyName').text.strip()
            except AttributeError:
                company_name_value = "Company name not found"

            try:
                location_value = job_seen_beacon.find('div', class_='companyLocation').text.strip()
            except AttributeError:
                location_value = "Location not found"
            try:
                salary_element = job_seen_beacon.find('div', class_='metadata').find('div', class_='attribute_snippet')
                salary_value = salary_element.text.strip() if salary_element else "Salary not found"        
            except AttributeError:
                salary_value = "salary not found"
            try:
                date_element = job_seen_beacon.find('span', class_='date')
                date_value = date_element.get_text(strip=True) if date_element else "Date not found"
                days_posted = re.findall(r'\d+', date_value)[0] if re.findall(r'\d+', date_value) else None
                
                if days_posted is not None:
                    actual_date = date.today() - timedelta(days=int(days_posted))
                    actual_date_str = actual_date.strftime('%Y-%m-%d')
                else:
                    actual_date_str = "Date not found"
            except AttributeError:
                date_value = "Date not found"


            salary_str = salary_value.replace('$', '').replace('por año', '').replace('por hora', '').replace('-', '').replace('a year', '').replace('an hour', '')

            if len(salary_str.split()) == 2:
                # Split the salary values into a list
                salary_values = salary_str.split()

                # Remove commas and convert to float
                salary_values = [float(value.replace(',', '')) for value in salary_values]

                # Calculate the mean of the salary range
                salary_mean = sum(salary_values) / 2

                # Update salary_str with the mean value
                salary_str = str(salary_mean)


            
            
            # Assign the scraped values to the shared variables
            # Create a dictionary for the current job and append it to the jobs list
            job_data = {
                'job_title': job_title_value,
                'company_name': company_name_value,
                'location': location_value,
                'salary': salary_str,
                'date_posted': actual_date_str
            }
            jobs.append(job_data)

            print("Job Title:", job_title_value)
            print("Company Name:", company_name_value)
            print("Location:", location_value)
            print("Salary:", salary_str)
            print("Date Posted:", days_posted)
            print("Actual Date:", actual_date_str)

            print("--------------------------------------")
    else:
        print("No job listings found on the page.")

    # Export the jobs list to the variables.py file
    with open('variables.py', 'a') as file:
        file.write(f"job_titles = {[job['job_title'] for job in jobs]}\n")
        file.write(f"company_names = {[job['company_name'] for job in jobs]}\n")
        file.write(f"locations = {[job['location'] for job in jobs]}\n")
        file.write(f"salaries = {[job['salary'] for job in jobs]}\n")
        file.write(f"dates = {[job['date_posted'] for job in jobs]}\n")

time.sleep(60)