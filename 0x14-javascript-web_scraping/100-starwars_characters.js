#!/usr/bin/node
const process = require('process');
const request = require('request');

const movie = process.argv[2];

const url1 = 'https://swapi-api.hbtn.io/api/people/';
const url2 = 'https://swapi-api.hbtn.io/api/films/' + movie + '/';

request(url1, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    people = JSON.parse(body).results;
    for (let i = 0; people[i]; i++) {
      for (let j = 0; people[i].films[j]; j++) {
        if (url2 === people[i].films[j]) {
          console.log(people[i].name);
        }
      }      
    }
  }
});
