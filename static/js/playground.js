//Drop Prevent Function
function cancel(e) {
  if (e.preventDefault) {
    e.preventDefault();
  }
  return false;
}
function clickFunction(){
	$('#output').html("");
	$('#total-costs span').text(0);
}

//Equals Button Function
function equalFunction(){
	var exChildren=$("#output").children();
	var arr=[];
	var operand='';
	for (var i=0; i<exChildren.length; i++){ 
		if (exChildren[i].innerHTML!='+' && exChildren[i].innerHTML!='-'&& exChildren[i].innerHTML!='x' && exChildren[i].innerHTML!='/'){
			arr.push(parseInt(exChildren[i].innerHTML));
		}
		else{
			operand=exChildren[i].innerHTML;
		}
	}

	//Operations Done
	var a1=arr[0];
	var a2=arr[1];
	if (operand=='+'){
		var result=a1+a2;
	}
	else if (operand=='-'){
		var result=a1-a2;
	}
	else if (operand=='x'){
		var result=a1*a2;
	}
	else if (operand=='/'){
		var result=a1/a2;
	}
	console.log(result)

var html='<div draggable="true" class="dragable-item" data-title="Box 9" data-price="9" id="vals">=</div><div draggable="true" class="dragable-item" data-title="Box 9" data-price="9" id="vals">'+result+'</div>';		
	$('#output').append(html);

}
//Main Function
$(document).ready(function() {

		var total_costs = 0;
		console.log(parseInt($(".textid").text()));
		refresh_total_costs(total_costs);
		// Get the #drop zone
		var drop = document.getElementById('drop');
		var draggedItem = null;
		// Add the Event Listener to each draggable item
		$('.dragable-item').each(function(index){
			$(this)[0].addEventListener('dragstart',function(e){
				draggedItem = jQuery(this);
				e.dataTransfer.setData('Text', this.id); // required otherwise doesn't work
			},false);
		});
			$('.dragable-operand').each(function(index){
			$(this)[0].addEventListener('dragstart',function(e){
				draggedItem = jQuery(this);
				e.dataTransfer.setData('Text', this.id); // required otherwise doesn't work
			},false);
		});
		// Reset onClick
		document.getElementById("reset").addEventListener("click",clickFunction);
		// Equals onClick
		document.getElementById("equals").addEventListener("click",equalFunction);
		drop.addEventListener('dragover', cancel);
		drop.addEventListener('dragenter', cancel);
		drop.addEventListener('drop', function (e) {
		   e.preventDefault();		   
		   if ($(draggedItem).data('title')=='inputBox'){
		   		console.log(document.getElementById("textid").innerHTML);
		   		var x= document.getElementById("textid").innerHTML;
		   		var html= ('<div id="iHTML" draggable="true" class="dragable-item" data-title="'+$(draggedItem).data('title')+'" data-price="'+$(draggedItem).data('price')+'">'+x+'</div>')		   
		   $('#output').append(html);
		   }		   
		   else{
		   var html= ('<div id="iHTML" draggable="true" class="dragable-item" data-title="'+$(draggedItem).data('title')+'" data-price="'+$(draggedItem).data('price')+'">'+$(draggedItem).data('price')+'</div>')		   
		   $('#output').append(html);
		   	}		
		  return false;
		});
});
