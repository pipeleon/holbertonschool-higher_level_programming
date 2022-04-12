#!/usr/bin/node
const process = require('process');
const request = require('request');

const movie = process.argv[2];

const url = 'https://swapi-api.hbtn.io/api/films/' + movie + '/';

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const people = JSON.parse(body).characters;
    for (let i = 0; people[i]; i++) {
      request(people[i], function (error, response, body) {
        if (error) {
          console.log(error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
