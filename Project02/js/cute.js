function rotate(){
    for(var i=1;i<11;i++) {
      (function (local_i) {
        setTimeout(function(){
          document.getElementById('first' + local_i).classList.add('rotate');
        }, 100 * local_i);
      })(i);
    }
  }
