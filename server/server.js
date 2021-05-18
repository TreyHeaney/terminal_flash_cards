const express = require('express');

const userRoutes = require('./routes/user');
const saveRoutes = require('./routes/saves');

const app = express();
const port = 4444;

app.use(express.json());

app.use('/', userRoutes);
app.use('/', saveRoutes);

app.listen(port, () => {
  console.log(`Server listening on port ${port}!`);
});
