	var fname=document.getElementById("fname");
	var lname=document.getElementById("lname");
	var pass=document.getElementById("pass");
	var cPass=document.getElementById("confirmpass");
	var confirmPass=document.getElementById("confirmpass");
	var email=document.getElementById("email");



	var button=document.getElementById("button");
	button.addEventListener("click", function(evt){

		 if (fname.value == "") {
			    evt.preventDefault();
		 		var change=document.getElementById('fname'); 
			    change.style.border = "1px solid red";
			    change.placeholder = "First Name is required"
			    return;
  		}	

		if (lname.value == "") {
			    evt.preventDefault();
		 		var change=document.getElementById('lname'); 
			    change.style.border = "1px solid red";
			    change.placeholder = "Last Name is required"
			    return;
  		}

		if (pass.value == "") {
			    evt.preventDefault();
		 		var change=document.getElementById('Passwords'); 
			    change.style.border = "1px solid red";
			    change.style.color = "red";
			    change.placeholder = "Password is required"
			    return;
  		}  			

		else if (pass.value.length < 8) {
		    evt.preventDefault();
	 		var change=document.getElementById('pass'); 
		    change.style.border = "1px solid red";
		    change.style.color = "red";
			alert('Password Length should be >=8')
			return ;
		}  			


		if (confirmPass.value !== pass.value) {
		    evt.preventDefault();
	 		var change=document.getElementById('confirmpass'); 
		    change.style.border = "1px solid red";
		    change.style.color = "red";
			alert('Password and Confirm Password do not match')
			return;
		}  			

		var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
		var ans=re.test(email.value);

		if (!ans) {
				evt.preventDefault();
				var change=document.getElementById('email'); 
			    change.style.border = "1px solid red";
			    change.style.color = "red";
			    alert('Enter valid email address')
			    return;
  		}	



	});