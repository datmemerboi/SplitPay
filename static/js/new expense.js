Actors = []
function expenseNaming(arg) {
	var name = document.createElement("H2");
	name.innerHTML = arg;
	document.getElementById('expense-details-name').innerHTML = null;
	document.getElementById('expense-details-name').appendChild( name );
}

function createActor(event) {
	if( event.keyCode===13 ){
		Actors.push( document.getElementById('actors-input').value );
		document.getElementById('actors-input').value = null;
		putInDiv( Actors );
	}
}
function putInDiv( Actors ){
	var divi = document.getElementById('actors-involved');
	divi.innerHTML = null;
	Actors.forEach( (actor)=>{
		var item = document.createElement('BUTTON');
		item.setAttribute('class', 'actor-item');

		var label = document.createElement('LABEL');
		label.innerHTML = actor;

		var deleteBtn = document.createElement('BUTTON');
		deleteBtn.setAttribute('class', 'delete-btn');
		deleteBtn.setAttribute('onclick', 'deleteItem(this)');
		deleteBtn.innerHTML = "x";

		item.appendChild(label);
		item.appendChild( deleteBtn );

		divi.appendChild( item );
	});
}
function deleteItem(arg) {
	var label = arg.parentNode.childNodes[0].innerHTML;
	Actors = Actors.filter( (value, index)=>{ return value != label;});
	document.getElementById('actors-involved').removeChild( arg.parentNode );
}

function submission(event) {
	console.log(Actors);
 	$.ajax({
      type: "POST",
      url: "/expense/create/",
      data: {
      	'name': document.getElementById('expense-name').value,
        'actors': Actors,
        // 'csrfmiddlewaretoken': '{{ csrf_token }}',
      },
      success: function () {
      	alert("Created Event");
      	window.location.href="/";
      }
    });
}