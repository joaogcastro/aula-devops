const Express = require('express');

const app = new Express();

app.get('/', (req, res) => {
    res.json({ message: 'Servidor Node no ar!'});
});

app.listen(3000, () => {
    console.log('Server listening on 3000');
})