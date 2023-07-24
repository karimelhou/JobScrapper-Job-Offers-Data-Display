<script setup>
import {ref, onMounted } from 'vue';

const jobs = ref([]);

//function to fetch the data from the api 
const fetchData = () => {
  fetch('http://localhost:3000/api/jobs/')
    .then((response) => response.json())
    .then((data) => {
      console.log('Fetched data:', data); // Log the fetched data to check the response

       // Parse and format the date for each job item
       data.forEach((job) => {
        const isoDate = job.date_posted; // Assuming date_posted is in ISO 8601 format
        const dateObject = new Date(isoDate);
        const formattedDate = dateObject.toISOString().slice(0, 10); // Get YYYY-MM-DD format
        job.date_posted = formattedDate;
      });
      
      jobs.value = data; // Assign the fetched data to the 'jobs' array
    })
    .catch((error) => {
      console.error('Error fetching data:', error);
    });
};



onMounted(() => {
  fetchData();
});
</script>

<template>
  <main>
    <h1>JOB INDEED SCRAPPER</h1>

    <div class="table-wrapper">
      <table class="fl-table">
        <thead>
          <tr>
            <th>ID</th>
            <th>Title</th>
            <th>Company</th>
            <th>Location</th>
            <th>Salary</th>
            <th>Date Posted</th>

          </tr>
        </thead>
        <tbody>
          <tr v-for="job in jobs" :key="job.id">
            <td>{{ job.id }}</td>
            <td>{{ job.title }}</td>
            <td>{{ job.company }}</td>
            <td>{{ job.location }} </td>
            <td>{{ job.salary }}</td>
            <td>{{ job.date_posted }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </main>
</template>

<style>
* {
  box-sizing: border-box;
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
}

body {
  font-family: Helvetica;
  -webkit-font-smoothing: antialiased;
}

h2 {
  text-align: center;
  font-size: 18px;
  text-transform: uppercase;
  letter-spacing: 1px;
  color: white;
  padding: 30px 0;
}

/* Table Styles */

.table-wrapper {
  margin: 10px 70px 70px;
  box-shadow: 0px 35px 50px rgba(0, 0, 0, 0.2);
}

.fl-table {
  border-radius: 5px;
  font-size: 12px;
  font-weight: normal;
  border: none;
  border-collapse: collapse;
  width: 100%;
  max-width: 100%;
  white-space: nowrap;
  background-color: white;
}

.fl-table td,
.fl-table th {
  text-align: center;
  padding: 8px;
}

.fl-table td {
  border-right: 1px solid #f8f8f8;
  font-size: 12px;
}

.fl-table thead th {
  color: #ffffff;
  background: #b68c60;
}


.fl-table thead th:nth-child(odd) {
  color: #ffffff;
  background: #324960;
}

.fl-table tr:nth-child(even) {
  background: #F8F8F8;
}

/* Responsive */

@media (max-width: 767px) {
  .fl-table {
    display: block;
    width: 100%;
  }

  .table-wrapper:before {
    content: "Scroll horizontally >";
    display: block;
    text-align: right;
    font-size: 11px;
    color: white;
    padding: 0 0 10px;
  }

  .fl-table thead,
  .fl-table tbody,
  .fl-table thead th {
    display: block;
  }

  .fl-table thead th:last-child {
    border-bottom: none;
  }

  .fl-table thead {
    float: left;
  }

  .fl-table tbody {
    width: auto;
    position: relative;
    overflow-x: auto;
  }

  .fl-table td,
  .fl-table th {
    padding: 20px .625em .625em .625em;
    height: 60px;
    vertical-align: middle;
    box-sizing: border-box;
    overflow-x: hidden;
    overflow-y: auto;
    width: 120px;
    font-size: 13px;
    text-overflow: ellipsis;
  }

  .fl-table thead th {
    text-align: left;
    border-bottom: 1px solid #f7f7f9;
  }

  .fl-table tbody tr {
    display: table-cell;
  }

  .fl-table tbody tr:nth-child(odd) {
    background: none;
  }

  .fl-table tr:nth-child(even) {
    background: transparent;
  }

  .fl-table tr td:nth-child(odd) {
    background: #F8F8F8;
    border-right: 1px solid #E6E4E4;
  }

  .fl-table tr td:nth-child(even) {
    border-right: 1px solid #E6E4E4;
  }

  .fl-table tbody td {
    display: block;
    text-align: center;
  }
}</style>