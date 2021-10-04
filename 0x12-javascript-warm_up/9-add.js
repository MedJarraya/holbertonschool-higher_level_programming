#!/usr/bin/node
function add (z, x) {
    return z + x;
  }
  const z = Number(process.argv[2]);
  const x = Number(process.argv[3]);
  console.log(add(z, x));
