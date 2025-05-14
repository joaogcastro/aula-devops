const express = require('express');
const axios = require('axios');

const app = express();
const host = '0.0.0.0'
const port = 3000;

app.get('/', (req, res) => {
    axios.get('http://python-api:5000/')
        .then(response => {
            console.log(`Sending response: ${response.data}`);
            res.send(response.data);
        })
        .catch(error => {
            console.error('Error fetching data from Flask API:', error);
            res.status(500).send('Error fetching data from Flask API');
        });
});

app.listen(port, host, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
