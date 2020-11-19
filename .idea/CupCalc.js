//Calculate total from given values
function chocolateTotal() {

  var flour_price = document.getElementById("flour").value;
  var cocoa_price = document.getElementById("cocoa").value;
  var sugar_price = document.getElementById("sugar").value;
  var eggs_price = document.getElementById("eggs").value;
  var mayo_price = document.getElementById("mayo").value;

  var flour_final = (2/(4.28)) * flour_price;
  var cocoa_final = 6 * cocoa_price;
  var eggs_fianl = (1/6) * eggs_price;
  var mayo_final = 8 * mayo_price;

  var total = flour_final + cocoa_final + sugar_price + eggs_price + mayo_price;
  //total = total.toFixed(2);

  //display the total
  document.getElementById("wholeTotal").style.display = "block";
  document.getElementById("total").innerHTML = total;

}

document.getElementById("wholeTotal").style.display = "none";

document.getElementById("calculate").onclick = function() {
  chocolateTotal();

};
