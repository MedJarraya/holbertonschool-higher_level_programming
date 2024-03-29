#!/usr/bin/node
// Completed tasks @author: @medjarraya
const x = require('request');

x.get(process.argv[2], (err, res, body) => {
  if (err) console.log(err);
  else {
    const computed = {};
    const todos = JSON.parse(body);
    todos.forEach(task => {
      if (task.completed) {
        if (!computed[task.userId]) computed[task.userId] = 1;
        else computed[task.userId] += 1;
      }
    });
    console.log(computed);
  }
});
