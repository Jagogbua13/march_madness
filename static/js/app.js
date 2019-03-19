

function bbwinner(home,away){
   
     var url =`/prediction/${home}/${away}`
     var data = d3.json(url).then(function(data){
         var winner = data.winner;
         var loser = data.loser;
         d3.select("h1>span").text(winner)
     });
     console.log(data)
     
     
         //console.log(data)
     ;
    
};



var submit = d3.select("#submit");

submit.on("click", function() {

    // Prevent the page from refreshing
    d3.event.preventDefault();

    // Select the input element and get the raw HTML node
    var inputElement = d3.select("#patient-form-input");
    var inputElement2 = d3.select("#patient-form-input2");
    // Get the value property of the input element
    var inputValue = inputElement.property("value");
    var inputValue2= inputElement2.property("value");
    console.log(inputValue);
    console.log(inputValue2)
    bbwinner(inputValue,inputValue2);


});