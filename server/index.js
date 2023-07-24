const express = require('express');
const mysql = require('mysql');
const bodyParser = require('body-parser');
const cors = require('cors'); // Import the cors middleware


const app = express();
const port = 3000;

app.use(cors());
app.use(bodyParser.json());

// MySQL configuration
const dbConfig = {
  host: 'localhost',
  user: 'root',
  database: 'indeed_data',
};

const connection = mysql.createConnection(dbConfig);

// Connect to the database
connection.connect((err) => {
  if (err) {
    console.error('Error connecting to the database:', err);
    return;
  }
  console.log('Connected to the database.');
});

// API endpoints

// GET all jobs
app.get('/api/jobs', (req, res) => {
  connection.query('SELECT * FROM jobs', (err, result) => {
    if (err) {
      console.error('Error fetching jobs:', err);
      res.status(500).json({ error: 'Internal server error' });
    } else {
      res.json(result);
    }
  });
});

// GET a single job by ID
app.get('/api/jobs/:id', (req, res) => {
  const jobId = req.params.id;
  connection.query('SELECT * FROM jobs WHERE id = ?', [jobId], (err, result) => {
    if (err) {
      console.error('Error fetching job:', err);
      res.status(500).json({ error: 'Internal server error' });
    } else if (result.length === 0) {
      res.status(404).json({ error: 'Job not found' });
    } else {
      res.json(result[0]);
    }
  });
});

// POST a new job
app.post('/api/jobs', (req, res) => {
  const newJob = req.body;
  connection.query('INSERT INTO jobs SET ?', newJob, (err, result) => {
    if (err) {
      console.error('Error inserting job:', err);
      res.status(500).json({ error: 'Internal server error' });
    } else {
      newJob.id = result.insertId;
      res.status(201).json(newJob);
    }
  });
});

// PUT (Update) an existing job by ID
app.put('/api/jobs/:id', (req, res) => {
  const jobId = req.params.id;
  const updatedJob = req.body;
  connection.query('UPDATE jobs SET ? WHERE id = ?', [updatedJob, jobId], (err, result) => {
    if (err) {
      console.error('Error updating job:', err);
      res.status(500).json({ error: 'Internal server error' });
    } else if (result.affectedRows === 0) {
      res.status(404).json({ error: 'Job not found' });
    } else {
      updatedJob.id = jobId;
      res.json(updatedJob);
    }
  });
});

// DELETE a job by ID
app.delete('/api/jobs/:id', (req, res) => {
  const jobId = req.params.id;
  connection.query('DELETE FROM jobs WHERE id = ?', [jobId], (err, result) => {
    if (err) {
      console.error('Error deleting job:', err);
      res.status(500).json({ error: 'Internal server error' });
    } else if (result.affectedRows === 0) {
      res.status(404).json({ error: 'Job not found' });
    } else {
      res.json({ message: 'Job deleted successfully' });
    }
  });
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
