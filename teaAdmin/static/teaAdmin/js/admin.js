

var wc  =  new WebSocket(`ws://${window.location.host}/ws/teatime/`)




wc.onopen = (e)=>{



    document.getElementsByClassName('socket')[0].style.display = 'none';


}

wc.onclose= (e)=>{


    document.getElementsByClassName('socket')[0].style.display = 'block';
}

wc.onerror = (e) =>{
    document.getElementsByClassName('socket')[0].style.display = 'block';
    document.getElementsByClassName('socket')[0].innerText = 'WebSocket error please check the connection once.';


}


wc.onmessage = (e)=>{

  let toEnter = document.getElementsByClassName('datatoenter')[0];
console.log(e);
    if(e.data == '1')
    {

        console.log('on');

        toEnter.innerHTML = ` <input type="checkbox" name="quiz" id="quiz" checked> <label for="quiz">Disable</label>
        <p class='bg-success mt-2 status'>Status : Your Quiz Application is Enabled.</p>`

    }else if(e.data == '0')
    {
        console.log('off');
        toEnter.innerHTML = `
        <input type="checkbox" name="quiz" id="quiz"> <label for="quiz">Enable</label>
        <p class='bg-danger mt-2 status'>Status : Your Quiz Application is Disbaled.</p>
        `

    }
}

let QuizEnableButton = document.getElementById('quiz')

QuizEnableButton.addEventListener('change',(e)=>{

    console.log('clciked',QuizEnableButton.checked)

 wc.send(QuizEnableButton.checked)
   

})



//for seraching in the table



    function myFunction() {
        var input, filter, table, tr, td, i, txtValue;
        input = document.getElementById("myInput");
        filter = input.value.toUpperCase();
        table = document.getElementById("myTable");
        tr = table.getElementsByTagName("tr");
        for (i = 0; i < tr.length; i++) {
          td = tr[i].getElementsByTagName("td")[0];
          if (td) {
            txtValue = td.textContent || td.innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
              tr[i].style.display = "";
            } else {
              tr[i].style.display = "none";
            }
          }       
        }
      }
