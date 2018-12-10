var readline = require('readline');
var fs = require('fs');
var lineno = 0;
var hb = [];
var myInterface = readline.createInterface({
  input: fs.createReadStream('Heartbeats.txt')
});

myInterface.on('line', function (line){
  lineno++;
  //console.log('Line number ' + lineno + ': ' + line);
  hb.push(line);   
});
myInterface.on('close', function (line){
  for (var i = 5; i < hb.length; i++)
  {
    if(hb[i] && hb[i-1] && hb[i-2] && hb[i-3] && hb[i-4] && hb[i-5] >= 80 && hb[i] && hb[i-1] && hb[i-2] && hb[i-3] && hb[i-4] && hb[i-5] <= 100)
    {
      console.log("Heartbeat is stable");
    }
    if(hb[i] && hb[i-1] && hb[i-2] && hb[i-3] && hb[i-4] && hb[i-5] < 80)
    {
      for(var e = 0; e <= 10; e++ )
      {
        console.log("HEARTBEAT IS CRITICALLY LOW!!! IMMEDIATE ASSISTANCE NEEDED");
      }
      return true;
    }
    if( hb[i] && hb[i-1] && hb[i-2] && hb[i-3] && hb[i-4] && hb[i-5] >= 120)
    {
      for(var e = 0; e <= 10; e++ )
      {
        console.log("HEARTBEAT IS CRITICALLY HIGH!!! IMMEDIATE ASSISTANCE NEEDED!!!");
      }
      return true;
     
    }
  }
  //console.log(hb);
  });
console.log("File has been read");
