# Job Scrapper and Job Offers Data Display

## Introduction

This project consists of two main parts: an Indeed scrapper written in Python and a Vue.js 3 application with a Node.js server that fetches and displays the job data stored in a MySQL database.

## Indeed Scrapper (Python)

The Indeed scrapper is implemented using Python and BeautifulSoup library. It is responsible for scraping job data from the Indeed website. To bypass security measures, the scrapper also utilizes scrappy api APIs to extract relevant job details such as job titles, company names, locations, salaries, and dates posted. After gathering the required information, the scrapper performs data analysis to ensure data quality and consistency.

The analyzed job data is then stored efficiently in a MySQL database using SQLAlchemy, which allows for seamless integration and quick retrieval of job offers.

## Vue.js 3 Application and Node.js Server

The frontend of this project is built using Vue.js 3, which provides an intuitive and reactive user interface. The Vue.js application, combined with a Node.js server, facilitates the retrieval of job data from the MySQL database and delivers it to the webpage for display.

The Node.js server acts as an intermediary layer between the Vue.js application and the MySQL database. It provides an API endpoint to fetch job data from the database and serves it in JSON format. The Vue.js application efficiently handles this data and renders it in a user-friendly format, allowing job seekers to access the latest job offers and stay informed about the job market trends.

## Installation

### Indeed Scrapper (Python)
To run the Indeed scrapper, follow these steps:

Install Python if you haven't already: https://www.python.org/downloads/
Install the required Python libraries using pip:

```
pip install beautifulsoup4
pip install requests
pip install sqlalchemy
pip install pymysql
```
Create a MySQL database named "indeed_data." <br>
Update the database connection details in the Python script:
```
engine = create_engine('mysql+pymysql://<username>:<password>@localhost/indeed_data') ````
Run the Python script to start the data scraping and storage process:
```
python indeed_scrapper.py ````

### Vue.js 3 Application and Node.js Server
To run the Vue.js 3 application and Node.js server, follow these steps:

Install Node.js if you haven't already: https://nodejs.org/en/download/ <br>
Navigate to the "vue-app" directory in your terminal or command prompt. <br>
Install the required Node.js packages for the Vue.js application: <br>
````
npm install ```
Install the required Node.js packages for the Node.js server: <br>
```
cd server
npm install ```
Update the database connection details in the Node.js server file "server.js":
```
const dbConfig = {
  host: 'localhost',
  user: '<username>',
  password: '<password>',
  database: 'indeed_data',
}; ```
Start the Node.js server:
```
node server.js ```
In a new terminal or command prompt, navigate back to the "vue-app" directory. <br>
Update the API endpoint in "src/views/crudView.vue" to match your Node.js server URL: <br>
````
const apiEndpoint = 'http://localhost:3000/api/jobs/';
```
Start the Vue.js application:
```
npm run dev ```
Open your web browser and access the application at http://localhost:3001/.  <br> <br>
The Vue.js application should now display the job data fetched from the Node.js server and formatted in a table.

## Contribution and License

This project is open-source, and contributions are welcome. If you use this project or its code, please consider giving credit to the original author, Karim ElHoumaini.

License: MIT License

For any questions or issues related to the project, feel free to contact the author at elhoumaini.ka@gmail.com.

Happy job data scrapping and displaying!
