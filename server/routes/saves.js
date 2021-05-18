// User save related routing.

const express = require('express');

const dbconn = require('../src/dbConnection');
const {userAuth} = require('../src/authorizations')

const router = express.Router();

router.post('/save', userAuth, (req, res) => {
  const file = req.body;
  console.log(file);
});

router.get('/save', userAuth, async (req, res) => {
});

module.exports = router;