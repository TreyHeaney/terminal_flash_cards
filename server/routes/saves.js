// User save related routing.

const express = require('express');

const dbconn = require('../src/dbConnection');
const {userAuth} = require('../src/authorizations')
const {createJson} = require('../src/saves');

const router = express.Router();

router.post('/save', userAuth, (req, res) => {
  const {id} = req.tokenKeys;
  const file = req.body;
  dbconn('saves').select('*').where({user_id: id})
    .then((rows) => {
      console.log(rows);
    })
});

router.get('/save', userAuth, async (req, res) => {
});

module.exports = router;