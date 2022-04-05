#!/usr/bin/node
exports.addMeMaybe = function (number, theFunction) {
  number++;
  String(number);
  theFunction(number);
};
