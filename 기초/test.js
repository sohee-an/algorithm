var a = "hello";
first();

function first() {
  var b = "hi";
  second();
  function second() {
    var c = "hey";

    third();
    function third() {
      var d = "so";
      console.log("hi", this);
      console.log(a + b + c + d);
    }
  }
}
