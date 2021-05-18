// User account related routing.

const express = require('express');
const crypto = require('crypto');

const dbconn = require('../src/dbConnection');
const {checkSignIn, hashPassword} = require('../src/authorizations')
const {createJson} = require('../src/saves');

const router = express.Router();

router.post('/sign_in', (req, res) => {
  console.log(req.body);
  const {user, password} = req.body;
  dbconn('users').select('*').where({user: user})
    .then((rows) => {
      checkSignIn(res, rows, password);
    })
    .catch((error) => {
      console.log(error);
      res.status(500).json({message: 'DB Error. Local save will be used.'});
    });
});

router.post('/sign_up', async (req, res) => {
  console.log(req.body);
  const {user, password} = req.body;
  const existingUser = await dbconn('users').select('*').where({user: user})

  if (existingUser.length > 0) {
    res.status(500).json({message: 'Username already in use.'});
    return;
  }

  const hash = await hashPassword(password)

  await dbconn('users').insert({
    user: user,
    password: hash,
  })

  const rows = await dbconn('users').select('id').where({user: user})
  const userID = rows[0].id;

  const fileName = await createJson();

  dbconn('saves').insert({
    user_id: userID,
    file: fileName,
  }).then(() => {
    res.status(201).json({message: 'Account successfully created!'});
  })
});

module.exports = router;