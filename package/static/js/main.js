console.log("111111111111")


$(document).ready(function(){
	$('button#elem1').click(function(){
		console.log('///')
		$('form#add_track').removeClass('d-none');
		console.log('///2')
		$('form#add_track').show();
		console.log('///3')
		

	})

	$("button#cancel1").click(function(){
		$('form#read_user_form').addClass('d-none');
		$('form#read_user_form').hide();
	})
	$("span#user").click(function(){
		$('form#read_user_form').removeClass('d-none');
		$('form#read_user_form').hide();
		$('form#read_user_form').show();
	})

   $(".fader").click(function(){
   	$("div#show").removeClass("d-none");
   	$("div.fader").children("div").hide();
    $(this).children("div").show();
  });
});


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

// clear()
