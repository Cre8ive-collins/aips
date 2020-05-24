console.log("111111111111")


function validateRegForm(name){
		valcount = 1;
		function isNumeric(n) {
  		return !isNaN(parseFloat(n)) && isFinite(n);
		}var matches = name.match(/\d+/g);
	var len = name.length; 
	if (name == ""){
			valcount ++;
			empty = document.getElementById("response");
			empty.innerHTML = "   &nbsp; &nbsp;Name cannot be blank";
			empty.setAttribute("class", "bg-danger fa fa-remove form-control text-light");
		}
	else if (len < 3){
		valcount ++;
		less = document.getElementById("response")
		less.setAttribute("class", "bg-danger fa fa-remove form-control text-light")
		less.innerHTML = " &nbsp; &nbsp; Name must contain minimum of 3 characters";
		}
	else if (matches != null) {
		valcount ++;
    	console.log('number');
    	num = document.getElementById("response");
		num.innerHTML = "   &nbsp; &nbsp;Name cannot contain number(s)";
		num.setAttribute("class", "bg-danger fa fa-remove form-control text-light");
		}
	else{
		valcount = 0;
		ok = document.getElementById("response");
		ok.innerHTML = "";
		ok.setAttribute("class", "text-success fa fa-check");
	}

	
	if (valcount == 0);
		btn = document.getElementById("submit");
		btn.setAttribute("class", "btn btn-success btn-lg form-control");

	
};

