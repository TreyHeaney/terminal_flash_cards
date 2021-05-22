// User save related routing.

const fs = require('fs');

const express = require('express');
const crypto = require('crypto');

const dbconn = require('../src/dbConnection');
const {userAuth} = require('../src/authorizations');
const { handleError } = require('../src/eventHandlers');

const router = express.Router();

router.post('/save', userAuth, (req, res) => {
  const {id} = req.tokenKeys;
  dbconn('saves').select('*').where({user_id: id})
    .then((rows) => {
      const fileName = rows[0].file;
      const data = JSON.stringify(req.body);
      fs.writeFileSync('./static/' + fileName + '.json', data);
      res.status(200).json({message: 'Updated save!'});
    })
    .catch((error) => handleError(error, res));
});

router.get('/save', userAuth, async (req, res) => {
  const {id} = req.tokenKeys;
  dbconn('saves').select('*').where({user_id: id})
    .then((rows) => {
      const fileName = rows[0].file;
      const rawdata = fs.readFileSync('./static/' + fileName + '.json');
      const save = JSON.parse(rawdata);

      res.status(200).json(save);
    })
    .catch((error) => handleError(error, res));
});

module.exports = router;