const express = require('express');

const app = express();
const port = 4444;

app.listen(port, () => {
  console.log(`Server listening on port ${port}!`);
});
