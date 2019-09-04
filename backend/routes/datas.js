var express = require('express');
var router = express.Router();
var mysql = require('mysql');

var connection = mysql.createConnection({
    host: '127.0.0.1',
    port: 3306,
    user: 'root',   
    password: 'wjdtjd864@',
    database: 'testdb'  
  }); 
  
  connection.connect(function (err) {   
    if (err) {     
      console.error('mysql connection error');     
      console.error(err);     
      throw err;   
    } 
  });

router.get('/', function (req, res, next) {
    connection.query('SELECT * FROM testdb.data_table', function(err, datas, fields) {
        if(!err){
          
          res.send(datas);
        }
        else
          console.log('Error!!', err);
      });
 
});
router.get('/:id', function (req, res, next) {
    var id= parseInt(req.params.id, 10)
    console.log('dsds'+id)
    connection.query('SELECT * FROM testdb.data_table WHERE id ="'+id+'"', function(err, print_data, fields) {
        if(!err){
           
          console.log(print_data);
          res.send(print_data);
        }
        else
          console.log('Error!!', err);
      });
 
});
module.exports = router;