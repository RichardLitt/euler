
function findMultiples(total, factor1, factor2) {
	sum = 0
	for (i = 0; i < total; i++ ) {
		if ((i % factor1 == 0) || (i % factor2 == 0)) {
			console.log(i)
			sum += i
		}
	}
	console.log("sum", sum)
	return sum
}

findMultiples(1000, 3, 5)
