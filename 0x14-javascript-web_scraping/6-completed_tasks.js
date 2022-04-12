#!/usr/bin/node
const process = require('process');
const request = require('request');

const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const allDict = JSON.parse(body);
    const newDict = {};
    for (let i = 1; i <= 1; i++) {
      for (let j = 0; allDict[j]; j++) {
        if (allDict[j].completed === true) {
          if (allDict[j].userId in newDict) {
            newDict[allDict[j].userId]++;
          } else {
            newDict[allDict[j].userId] = 1;
          }
        }
      }
    }
    console.log(newDict);
  }
});
