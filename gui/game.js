var d3 = require('d3');
var $= require('jquery');
var dummy=[{'pos':[0,0],'piece':'a'},{'pos':[0,1],'piece':'b'},{'pos':[0,2],'piece':'c'},{'pos':[0,3],'piece':'d'},{'pos':[0,4],'piece':'e'},
                {'pos':[1,0],'piece':'f'},{'pos':[1,1],'piece':'g'},{'pos':[1,2],'piece':'h'},{'pos':[1,3],'piece':'i'},{'pos':[1,4],'piece':'j'},
                {'pos':[2,0],'piece':'k'},{'pos':[2,1],'piece':'l'},{'pos':[2,2],'piece':'m'},{'pos':[2,3],'piece':'n'},{'pos':[2,4],'piece':'o'}]

var margin = {top: 20, right: 40, bottom: 30, left: 20},
            width = 500 - margin.left - margin.right,
            height = 300 - margin.top - margin.bottom;
var x=d3.scaleLinear()
    .domain([0, 5])
    .range([30, width]);
var y=d3.scaleLinear()
    .domain([0, 3])
    .range([30, height]);
var svg = d3.select("#gameboard").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
initGameBoard(dummy);


function updateData(){
    var dummy=[{'pos':[0,0],'piece':'a'},{'pos':[0,1],'piece':'b'},{'pos':[0,2],'piece':'c'},{'pos':[0,3],'piece':'e'},{'pos':[0,4],'piece':'d'},
            {'pos':[1,0],'piece':'f'},{'pos':[1,1],'piece':'g'},{'pos':[1,2],'piece':'h'},{'pos':[1,3],'piece':'i'},{'pos':[1,4],'piece':'j'},
            {'pos':[2,0],'piece':'k'},{'pos':[2,1],'piece':'l'},{'pos':[2,2],'piece':'m'},{'pos':[2,3],'piece':'n'},{'pos':[2,4],'piece':'o'}]
    initGameBoard(dummy);  
}
function initGameBoard(data){
    
              
   
   

   
    var oned=function(i){
        return [Math.floor(i/5),i%5];
    }
    var row=svg.selectAll("circle").data(data,d=>d.piece)
 
    var row_update=row.transition()
    .duration(750).attr("cx",(d,i)=>x(oned(i)[1]))
        .attr("cy",(d,i)=>y(oned(i)[0]))
        .attr("display",d=>d.piece=='e'?'none':'')
     
    var row_enter=row.enter()
        .append("circle")
        .attr("class", "pieces")
        .attr("cx",(d,i)=>x(oned(i)[1]))
        .attr("cy",(d,i)=>y(oned(i)[0]))
        .attr("display",d=>d.piece=='e'?'none':'')
        .attr("r",30);
   

    console.log("done");
}
