var d3 = require('d3');
var $= require('jquery');
var dummy=[{'pos':[0,0],'piece':'a'},{'pos':[0,1],'piece':'b'},{'pos':[0,2],'piece':'c'},{'pos':[0,3],'piece':'d'},{'pos':[0,4],'piece':'e'},
                {'pos':[1,0],'piece':'f'},{'pos':[1,1],'piece':'g'},{'pos':[1,2],'piece':'h'},{'pos':[1,3],'piece':'i'},{'pos':[1,4],'piece':'j'},
                {'pos':[2,0],'piece':'k'},{'pos':[2,1],'piece':'l'},{'pos':[2,2],'piece':'m'},{'pos':[2,3],'piece':'n'},{'pos':[2,4],'piece':'o'}]

var margin = {top: 0, right:0, bottom: 0, left: 0},
            width =600 - margin.left - margin.right,
            height = 370 - margin.top - margin.bottom;
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
    var g=svg.selectAll("g").data(data,d=>d.piece)
 

    var gEnter = g.enter().append("g");
   
    g.select(".r-piece").transition()
        .duration(750).attr("x",(d,i)=>x(oned(i)[1]))
        .attr("y",(d,i)=>y(oned(i)[0]))
        .attr("display",d=>d.piece=='e'?'none':'')

    g.select(".r-bot").transition()
        .duration(750).attr("x",(d,i)=>x(oned(i)[1])+4)
        .attr("y",(d,i)=>y(oned(i)[0])+88)
        .attr("display",d=>d.piece=='e'?'none':'')
    g.select(".piece-text").transition()
    .duration(750)
        .attr("x",(d,i)=>x(oned(i)[1]))
        .attr("y",(d,i)=>y(oned(i)[0]))
 
    gEnter.append("rect")
        .attr("class", "r-piece")
        .attr("x",(d,i)=>x(oned(i)[1]))
        .attr("y",(d,i)=>y(oned(i)[0]))
        .attr("display",d=>d.piece=='e'?'none':'')
        .attr("height",100)
        .attr("width",100)
        .attr("rx",16)
        .attr("ry",16);
    gEnter.append("rect")
        .attr("class", "r-bot")
        .attr("x",(d,i)=>x(oned(i)[1])+4)
        .attr("y",(d,i)=>y(oned(i)[0])+88)
        .attr("display",d=>d.piece=='e'?'none':'')
        .attr("height",12)
        .attr("width",92)
        .attr("rx",18)
        .attr("ry",30);
    gEnter.append("text").text("R")
        .attr("display",d=>d.piece=='e'?'none':'')
        .attr("x",(d,i)=>x(oned(i)[1])+40)
        .attr("y",(d,i)=>y(oned(i)[0])+50)
        .attr("class", "piece-text")

   
         
    
   

   
}
