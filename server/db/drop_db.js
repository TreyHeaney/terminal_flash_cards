const conn = {
  host: 'localhost',
  user: 'root',
  password: '',
};

const dbconn = require('knex')({client: 'mysql', connection: conn});

dbconn.raw('DROP DATABASE flash_cards')
  .then(() =>{
    console.log('DROPPED DATABASE');
    dbconn.destroy();
  });
