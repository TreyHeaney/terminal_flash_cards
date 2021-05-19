const express = require('express');

const userRoutes = require('./routes/user');
const saveRoutes = require('./routes/saves');

const app = express();
const port = 4444;

app.use(express.json());

app.use((req, res, next) => {
  const {originalUrl, method} = req;
  const spacing = originalUrl.length > 18 ? '' : ' '.repeat(20 - originalUrl.length);
  console.log(Date.now(), '      ', originalUrl, spacing, method);
  next();
});
app.use('/', userRoutes);
app.use('/', saveRoutes);

app.listen(port, () => {
  console.log(`Server listening on port ${port}!`);
});
