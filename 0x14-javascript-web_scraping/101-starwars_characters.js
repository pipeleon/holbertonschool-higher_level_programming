#!/usr/bin/node
const process = require('process');
const request = require('request');

const movie = process.argv[2];

const url = 'https://swapi-api.hbtn.io/api/films/' + movie + '/';

function searchUrlPeople (url) {
  return new Promise((resolve, reject) => {
    request(url, function (error, response, body) {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body).characters);
      }
    });
  });
}

function searchUrlName (url) {
  return new Promise((resolve, reject) => {
    request(url, function (error, response, body) {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body).name);
      }
    });
  });
}

async function printPeople (url) {
  const people = await searchUrlPeople(url);

  for (let i = 0; people[i]; i++) {
    const name = await searchUrlName(people[i]);
    console.log(name);
  }
}

printPeople(url);
