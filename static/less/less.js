var less = require('less');

less.render(
  '@import "less/style.less";',
  function (e, output) {
    var style = document.createElement('style');
    style.textContent = output.css;
    document.head.appendChild(style);
  }
);