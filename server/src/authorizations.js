const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

const jwtKey = require('../keys/jwtKey');

/**
 * Check a password against a stored hash relative to an email.
 * @param  {Object} res
 * @param  {Object} rows
 * @param  {String} password
 */
 function checkSignIn(res, rows, password) {
    if (rows.length == 1) {
      const {pwhash, id, email, type, verified} = rows[0];
      bcrypt.compare(password, pwhash, function(err, goodSignIn) {
        if (!err && goodSignIn) {
          if (!verified) {
            res.status(511).json({message: 'Email address unverified'});
            return;
          }
          const authorization = jwt.sign({
            id: id,
            email: email, // Consider removing this, it takes up a lot of network.
            type: type,
          },
          jwtKey,
          {expiresIn: '1d'});
  
          res.status(200).json({
            message: 'Login successful!',
            authorization: authorization,
          });
        } else {
          handleFailedSignin(res);
        }
      });
    } else {
      handleFailedSignin(res);
    }
  }