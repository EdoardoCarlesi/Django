// various commands

var array = ["cazzo", "figa", "gianfredo"]

for (var ar of array){

	console.log(ar)
}


// Objects i.e. dictionary + methods
var carCar = {car:"CarCar", wheels:"3"}

carCar["car"]


var cazzone = {propretario:"Cane",
		size:"21",
		
		// Object method
		scopare: function(){
			return this.size;
		}
	};

console.log(cazzone.scopare());
