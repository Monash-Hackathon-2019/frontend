
const spawn = require("child_process").spawn;
const pythonProcess = spawn('python',["./scraper.py"])

var fs = require('fs');
var i = 0;

while(!fs.existsSync('100.txt')){
	i++;
	if(i==100){
		i=0;
	}
	console.log(i)
}

var textByLine = fs.readFileSync('100.txt').toString();
console.log(textByLine);