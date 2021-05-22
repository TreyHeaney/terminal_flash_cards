const crypto = require('crypto');

module.exports = {
  handleError,
}

function handleError(error, res) {
  const supportCode = crypto.randomBytes(4).toString('hex');
  console.log(error, supportCode);
  res.status(500).json({message: supportCode})
}