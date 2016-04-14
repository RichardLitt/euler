function findPrimes (input) {
  var factor = []
  for (var i = 2; i < Math.sqrt(input); i++) {
    if (input % i === 0) {
      if (findPrimes(i).length === 0) {
        factor.push(i)
      }
    }
  }
  return factor
}

var result = findPrimes(process.argv[2])

console.log(result[result.length - 1])
