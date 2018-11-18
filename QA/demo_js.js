var graph = function()
{
  this.storage = {};
  this.size = 0;
}
graph.prototype.add = function (value)
{
  this.storage[value] = {};
  this.size ++;
}
graph.prototype.addConnection = function(time, hb)
{
  this.storage[time][hb]=0;
  //this.storage[hb][time]= true;
}


var TimeHeart = new graph();
for(var i = 0; i < 100; i++)
{
  TimeHeart.add(i);
}
for(var i = 0; i < 100; i++)
{
  if( (i % 2) == 0)
  {
    TimeHeart.addConnection(i, 98);
  }
  else
  {
    TimeHeart.addConnection(i, 99);
  }
}

console.log(TimeHeart);
