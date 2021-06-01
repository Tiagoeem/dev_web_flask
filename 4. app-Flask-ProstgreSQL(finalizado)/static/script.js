//https://codepen.io/tag/formulario

form.addEventListener('submit', (e) => {
  e.preventDefault();
  	const form = document.getElementById('form');

	const nome = document.getElementsByName("nome")[0].value;
	const sobrenome = document.getElementsByName("sobre")[0].value;
	const cpf = document.getElementsByName("cpf")[0].value;


// ----- Direto do postman
  	var myHeaders = new Headers();
	myHeaders.append("Content-Type", "application/json");

	var raw = JSON.stringify({
	  "sobrenome": sobrenome,
	  "primeiro_nome": nome,
	  "cpf": cpf
	});

	var requestOptions = {
	  method: 'POST',
	  headers: myHeaders,
	  body: raw,
	  redirect: 'follow'
	};

	// ----- caminho relativo
	fetch("../cliente", requestOptions)
	  .then(response => response.text())
	  .then(result => console.log(result))
	  .catch(error => console.log('error', error))
});

