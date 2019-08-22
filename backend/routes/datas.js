var express = require('express');
var router = express.Router();
var datas = require('../datas.json');

router.get('/', function (req, res, next) {
 res.send(datas)
});

module.exports = router;