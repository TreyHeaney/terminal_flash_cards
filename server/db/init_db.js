const conn = {
  host: 'localhost',
  user: 'root',
  password: '',
};

let dbconn = require('knex')({client: 'mysql', connection: conn});

dbconn.raw('CREATE DATABASE IF NOT EXISTS flash_cards')
  .then(async () => {
    await dbconn.destroy();
    dbconn = require('../src/dbConnection');

    await dbconn.raw(`
    CREATE TABLE IF NOT EXISTS users (
      id        INT           AUTO_INCREMENT,
      user      VARCHAR(20)   NOT NULL,
      password  VARCHAR(100)  NOT NULL,
      PRIMARY KEY (id)
    );
    `);
    await dbconn.raw(`
    CREATE TABLE IF NOT EXISTS saves (
      user_id   INT           NOT NULL,
      file      TEXT          NOT NULL,
      CONSTRAINT \`fkey_saves_users\`
      FOREIGN KEY (user_id)
      REFERENCES users(id)
      ON UPDATE CASCADE
      ON DELETE CASCADE
    );
    `);
    await dbconn.raw(`
    INSERT INTO users (user, password) VALUES (
      'trey', '$2b$12$bVNbKvaNkTMoOtDftmGH/uX5HHe/nF6f0jfVFsv7GCfPRWUiG9vKa'
    );
    `);
    await dbconn.raw(`
    INSERT INTO saves VALUES (
      1,
      '123456789'
    );
    `);

    console.log('CREATED DATABASE');

    dbconn.destroy();
  })