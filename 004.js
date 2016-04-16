function reverse (s) {
  return s.toString().split('').reverse().join('')
}

function findPalindromes () {
  var palindrome = 0
  for (var i = 100; i < 1000; i++) {
    for (var k = 100; k < 1000; k++) {
      var product = i * k
     if (product == reverse(product) && product > palindrome) {
        palindrome = product
      }
    }
  }
  console.log(palindrome)
}

findPalindromes()
