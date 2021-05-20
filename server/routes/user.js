// User account related routing.

const express = require('express');
const crypto = require('crypto');

const dbconn = require('../src/dbConnection');
const {checkSignIn, hashPassword} = require('../src/authorizations')
const {createJson} = require('../src/filesystem');
const {handleError} = require('../src/eventHandlers');

const router = express.Router();

router.post('/sign_in', (req, res) => {
  const {user, password} = req.body;
  console.log(req.body);
  dbconn('users').select('*').where({user: user})
    .then((rows) => {
      checkSignIn(res, rows, password);
    })
    .catch((error) => handleError(error, res));
});

router.post('/sign_up', async (req, res) => {
  const {user, password} = req.body;
  const existingUser = await dbconn('users').select('*').where({user: user})
    .catch((error) => handleError(error, res));

  if (existingUser.length > 0) {
    res.status(500).json({message: 'Username already in use.'});
    return;
  }

  const hash = await hashPassword(password)
    .catch((error) => handleError(error, res));

  await dbconn('users').insert({
    user: user,
    password: hash,
  }).catch((error) => handleError(error, res))

  const rows = await dbconn('users').select('id').where({user: user})
    .catch((error) => handleError(error, res));
  const userID = rows[0].id;

  const fileName = await createJson();

  dbconn('saves').insert({
    user_id: userID,
    file: fileName,
  }).then(() => {
    res.status(201).json({message: 'Account successfully created! You can now sign in.'});
  }).catch((error) => handleError(error, res));
});

module.exports = router;
