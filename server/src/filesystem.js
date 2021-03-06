const fs = require('fs');
const crypto = require('crypto');

module.exports = {
  createJson,
}

function createJson() {
  return new Promise(async (resolve, reject) => {
    const date = Date.now().toString();
    const hash = crypto.randomBytes(4).toString('hex');
    const fileName = date + hash;

    let data = JSON.stringify({});
    fs.writeFileSync('./static/' +  fileName + '.json', data);

    resolve(fileName);
  });
}