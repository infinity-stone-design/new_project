var express = require('express');
var router = express.Router();
var mysql = require('mysql');

var connection = mysql.createConnection({
    host: '127.0.0.1',
    port: 3306,
    user: 'root',   
    password: 'duddlsdud1',
    database: 'data'  
  }); 
  
  connection.connect(function (err) {   
    if (err) {     
      console.error('mysql connection error');     
      console.error(err);     
      throw err;   
    } 
  });

router.get('/', function (req, res, next) {
    connection.query('SELECT * FROM data.table', function(err, datas, fields) {
        if(!err){
          console.log(datas);
          res.send(datas);
        }
        else
          console.log('Error!!', err);
      });
 
});

module.exports = router;