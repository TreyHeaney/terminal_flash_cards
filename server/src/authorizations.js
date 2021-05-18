const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

const jwtKey = require('../keys/jwtKey');

module.exports = {
  checkSignIn,
  hashPassword,
  userAuth,
}

/**
 * Check a password against a stored hash relative to an email.
 * @param  {Object} res
 * @param  {Object} rows
 * @param  {String} password
 */
function checkSignIn(res, rows, unhashed_password) {
  if (rows.length > 0) {
    const {password, id} = rows[0];
    bcrypt.compare(unhashed_password, password, function(err, goodSignIn) {
      console.log(err, goodSignIn)
      if (!err && goodSignIn) {
        const authorization = jwt.sign({
          id: id,
        },
        jwtKey,
        {expiresIn: '1w'});

        res.status(200).json({
          message: 'Login successful!',
          authorization: authorization,
        });
      } else {
        res.status(500).json({message: 'Incorrect password.'});
      }
    });
  } else {
    res.status(500).json({message: 'Account not found.'});
  }
}
/**
 * Hash a password.
 * @param {String} password Password to hash.
 * @returns {Promise} A promise that resolves with a hash.
 */
function hashPassword(password) {
  return new Promise((resolve, reject) => {
    bcrypt.hash(password, 10, (error, hash) => {
      if (error) {
        reject(error);
      } else {
        resolve(hash);
      }
    });
  })
}

/**
 * Check if the current user is authorized to access the next route and parse their token.
 * @param  {Object} req  An express request object.
 * @param  {Object} res  An express response object.
 * @param  {Object} next An express next object.
 */
 function userAuth(req, res, next) {
  try {
    const decoded = jwt.verify(req.headers.authorization, jwtKey);
    req.tokenKeys = decoded;
    next();
  } catch (error) {
    res.status(401).json({message: 'Please login.'});
  }
}
