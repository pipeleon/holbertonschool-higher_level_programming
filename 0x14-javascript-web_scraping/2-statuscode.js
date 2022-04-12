#!/usr/bin/node
const process = require('process');
const request = require('request');

const urlPath = process.argv[2];

request(urlPath, function (error, response) {
  if (error) {
    console.log(error);
  } else {
    console.log('code: ', response.statusCode);
  }
});
