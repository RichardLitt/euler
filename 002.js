function evenFiboSummed(numMax) {
  for (var sum = 0, i = 0, j = 1, k = 0; sum < numMax; k++) {
    var x = i + j
    console.log('x', x)
    if (x % 2 === 0) {
      sum += x
      console.log('sum', sum)
    }
    i = j
    j = x
  }
}

evenFiboSummed(4000000)
