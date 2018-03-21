var d3 = require('d3');
var $ = require('jquery');
var reader = require("buffered-reader");
const path = require('path')
var auto_var=false;
var move_i=0;
var uint8arrayToString = function (data) {
    return String.fromCharCode.apply(null, data);
};
var board_list = [['A', 'B', 'C', 'D', 'E'],
['F', 'G', 'H', 'I', 'J'],
['K', 'L', 'M', 'N', 'O']]
var enc = new TextEncoder("utf-8");
const spawn = require('child_process');

const scriptExecution = spawn.spawn('../dist/candyCrisis.exe');
// const fileReader = new reader.DataReader("../dist/output.txt", { encoding: "utf8" })
//     .on("error", function (error) {
//         console.log("error: " + error);
//     })
//     .on("line", function (line) {
//         $("#output").append(" <div class='console_output'>" +line + "</div>");

//     })
//     .on("end", function () {
//         console.log("EOF");
//     })
//     .read();
var margin = { top: 0, right: 0, bottom: 0, left: 0 },
    width = 600 - margin.left - margin.right,
    height = 370 - margin.top - margin.bottom;
var x = d3.scaleLinear()
    .domain([0, 5])
    .range([30, width]);
var y = d3.scaleLinear()
    .domain([0, 3])
    .range([30, height]);
var svg = d3.select("#gameboard").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)


var board = [];



var emptyPiece;
var emptyPiecePos;
var clickedPiece;
scriptExecution.stdout.on('data', function (data) {
    message = uint8arrayToString(data).split("\n");

    for (var i = 0; i < message.length; i++) {
        if (message[i].substr(0, 3) == "CON") {
            setTimeout(() => { 
                alert("You won!");
                svg.selectAll("*").remove()
                auto_var=false;
                move_i=0;
                scriptExecution.stdin.write( "\n");

                
            },auto_var?250*(move_i+1.2):0);
        }
        if(message[i].substr(0, 5) == "[Turn"){
            //move_i = parseInt(message[i].slice(8, 10));
            if(auto_var) move_i++;
            console.log(move_i)
        }
        if (message[i].slice(0, 8) == "Solution"){
            $("#output").append(" <div class='console_output'>" + message[i] + "</div>");

        }
        if (message[i].substr(0, 2) == "[[") {
           
            message[i] = message[i].replace(/'/g, '"');
            board = JSON.parse(message[i]);
            
            if(auto_var){
            
                initGameBoard(board);
              
            }
                 
            else{
               initGameBoard(board);

            }
        }
    }


});
scriptExecution.on('error', function (err) {
    console.log(err);
});


function auto(){
    auto_var=true;
    scriptExecution.stdin.write("auto" + "\n");

}

function updateData() {
    initGameBoard(dummy);
}
function initGameBoard(data) {






    var oned = function (i) {
        return [Math.floor(i / 5), i % 5];
    }
    var g = svg.selectAll("g").data(data, d => d[0])
    svg.selectAll("rect").data(data).enter().append("rect")
        .attr("class", "empty-field")
        .attr("x", (d, i) => x(oned(i)[1]))
        .attr("y", (d, i) => y(oned(i)[0]))
        .attr("height", 100)
        .attr("width", 100)
        .attr("rx", 16)
        .attr("ry", 16);

    var gEnter = g.enter().append("g");

    g.select(".pieces").transition()
        .duration(300).attr("x", (d, i) => x(oned(i)[1])  ).delay(()=>{
            var delay=250*move_i
            return auto_var?delay:0
        })
        .attr("y", (d, i) => y(oned(i)[0]))
        .attr("display", d => d[1] == 'e' ? 'none' : '');

    g.select(".bots").transition()
        .duration(300).attr("x", (d, i) => x(oned(i)[1]) + 4).delay(()=>{
            var delay=250*move_i
            return auto_var ? delay : 0
        })
        .attr("y", (d, i) => y(oned(i)[0]) + 88)
        .attr("display", d => d[1] == 'e' ? 'none' : '')
    g.select(".piece-text").transition()
        .duration(300).delay(()=>{
            var delay=250*move_i
            return auto_var ? delay : 0
        })
        .attr("x", (d, i) => x(oned(i)[1]) + 35)
        .attr("y", (d, i) => y(oned(i)[0]) + 60);

    gEnter.append("rect")
        .attr("class", d => d[1] + "-piece pieces")
        .attr("x", (d, i) => x(oned(i)[1]))
        .attr("y", (d, i) => y(oned(i)[0]))
        .attr("display", d => d[1] == 'e' ? 'none' : '')
        .attr("height", 100)
        .attr("width", 100)
        .attr("rx", 16)
        .attr("ry", 16)
        .on("click", (d, i) => {
            var p = board.findIndex(e => e[0] == d[0])
            var move = board_list[oned(p)[0]][oned(p)[1]]
            scriptExecution.stdin.write(move+"\n");


        });


    gEnter.append("rect")
        .attr("class", d => d[1] + "-bot bots")
        .attr("x", (d, i) => x(oned(i)[1]) + 4)
        .attr("y", (d, i) => y(oned(i)[0]) + 88)
        .attr("display", d => d[1] == 'e' ? 'none' : '')
        .attr("height", 12)
        .attr("width", 92)
        .attr("rx", 18)
        .attr("ry", 30);
    gEnter.append("text").text(d => d[1])
        .attr("display", d => d[1] == 'e' ? 'none' : '')
        .attr("x", (d, i) => x(oned(i)[1]) + 35)
        .attr("y", (d, i) => y(oned(i)[0]) + 60)
        .attr("class", "piece-text")









}