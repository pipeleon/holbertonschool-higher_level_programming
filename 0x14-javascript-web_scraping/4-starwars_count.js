#!/usr/bin/node
const process = require('process');
const request = require('request');

const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let count = 0;
    const movies = JSON.parse(body).results;
    for (let j = 0; movies[j]; j++) {
      for (let i = 0; movies[j].characters[i]; i++) {
        if (movies[j].characters[i] === 'https://swapi-api.hbtn.io/api/people/18/' || movies[j].characters[i] === 'http://swapi-api.hbtn.io/api/people/18/') {
          count++;
        }
      }
    }
    console.log(count);
  }
});
