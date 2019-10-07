// DAILY CODING PROBLEM

// 1.1
const arr = [1,2,3, 4, 5,6,7]
const sumMultiplied1 = (arr) => arr.reduce( (prev, next) => prev * next )
const sum = sumMultiplied1(arr)
const calculate = (arr) => arr.map( (elem, _) => sum / elem)

console.log("Array:", arr, "\n")

// 1.2
// sumLeft, sumRight
const sumMultiplied2 = ((sum) => (value) => sum *= value )
const sumLeft = arr.map(sumMultiplied2(1))
const sumRight = arr.slice().reverse().map(sumMultiplied2(1)).reverse()

const calculateWithoutDivision = (arr) => arr.map( (elem, i) => {
  var left = i > 0 ? sumLeft[i-1] : 1
  var right = i < arr.length-1 ? sumRight[i+1] : 1
  return left * right
})

console.log('Version with division:', calculate(arr), "\n")
console.log('Version without division:', calculateWithoutDivision(arr))
