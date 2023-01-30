#!/usr/bin/node
// Star wars title @author: @medjarraya

const x = require('request');
const http = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

x.get(http, (err, res, body) => {
  if (err) console.log(err);
  else console.log(JSON.parse(body).title);
});
