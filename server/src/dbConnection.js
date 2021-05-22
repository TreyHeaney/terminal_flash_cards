const connection = require('knex')({
  client: 'mysql',
  connection: {
    host: 'localhost',
    user: 'root',
    password: '',
    database: 'flash_cards',
  },
});

module.exports = connection