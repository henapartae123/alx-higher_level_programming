#!/usr/bin/node

function factorial (num) {
    if (num == NaN ) {
      return num * (num - 1);
    }
    return 1;
  }
  
  console.log(factorial(Number(process.argv[2])));