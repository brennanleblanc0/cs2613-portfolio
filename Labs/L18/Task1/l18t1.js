class City {
	constructor(name, population) {
		this.name = name;
		this.population = population;
	}
	equals(compCity) {
		return (this.name === compCity.name && this.population == compCity.population);
	}
}

class CityMap{
	constructor(){
		this.adjacencyList = [];
	}

	addConnection(startCity, endCity, dist){
		//Adding first connection
		if(this.adjacencyList.length == 0){
			this.adjacencyList[0] = [startCity, [endCity], [dist]];
			this.adjacencyList[1] = [endCity, [startCity], [dist]];
		}
		else{
			//Check to see if startCity is in list
			let startCityFound = -1;
			for(let i = 0; i < this.adjacencyList.length; i++){
				if(this.adjacencyList[i][0].equals(startCity)){
					startCityFound = i;
					break;
				}
			}
			//startCity already registered in list
			if(startCityFound >= 0){
				this.adjacencyList[startCityFound][1][this.adjacencyList[startCityFound][1].length] = endCity;
				this.adjacencyList[startCityFound][2][this.adjacencyList[startCityFound][2].length] = dist;
			}
			//startCity is not registered
			else{
				this.adjacencyList[this.adjacencyList.length] = [startCity, [endCity], [dist]];
			}

			let endCityFound = -1;
			for(let i = 0; i < this.adjacencyList.length; i++) {
				if (this.adjacencyList[i][0].equals(endCity)) {
					endCityFound = i;
					break;
				}
			}

			if (endCityFound >= 0) {
				this.adjacencyList[endCityFound][1][this.adjacencyList[endCityFound][1].length] = startCity;
				this.adjacencyList[endCityFound][2][this.adjacencyList[endCityFound][2].length] = dist;
			} else {
				this.adjacencyList[this.adjacencyList.length] = [endCity, [startCity], [dist]]
			}
		}
	}

	printMap() {
		for (let i=0; i < this.adjacencyList.length; i++) {
			console.log("%s", this.adjacencyList[i][0].name);
			for (let j=0; j < this.adjacencyList[i][1].length; j++) {
				console.log("\t%s (%dkm)", this.adjacencyList[i][1][j].name, this.adjacencyList[i][2][j]);
			}
		}
	}
}

//Main code goes here...

const bathurst = new City("Bathurst", 11897);
const miramichi = new City("Miramichi", 17537);
const edmundston = new City("Edmundston", 16580);
const campbellton = new City("Campbellton", 6883);


let map = new CityMap();
map.addConnection(bathurst, miramichi, 75.9);
map.addConnection(bathurst, edmundston, 248);
map.addConnection(bathurst, campbellton, 108);
map.addConnection(edmundston, campbellton, 200);


map.printMap();
