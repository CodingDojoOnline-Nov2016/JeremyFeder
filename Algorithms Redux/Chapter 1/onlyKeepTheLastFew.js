// Only Keep the Last Few
// Stan learned something today: that reducing an array’s .length immediately shortens it by that amount. Given array arr and number X, remove all except the last X elements, and return arr (changed and shorter). Given ([2,4,6,8,10],3), change the given array to [6,8,10] and return it.



function remAllButLastX(arr, x) {
	var temp = [];
	for(i = arr.length - x; i < arr.length; i++) {
		temp.push(arr[i]);
	}
	arr = temp;
	console.log(arr);
	return arr;
}

var array = [2,4,6,8,10];
remAllButLastX(array, 3);


//for loop broken down:  i = arr.length (which is 5) minus x (which is 3) = 2.  So i=2 to start.  Start at index of 2.
