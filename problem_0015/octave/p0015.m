%to reach the lower, right corner in a 20x20 grid with only (r|d) moves,
%you need a sequence of 20 right and 20 down moves, the order of which is not important
%
%thus: we are looking for the number of possible combinations in an array of 40 elements,
%with only two types of elements (e.g. a bit array) and an equal number of the first kind
%of elements and the second kind of elements
%
%i.e. the question could also be "how many 40 element bit arrays with exactly 20 1's are there?"
%
%this can be calculated with the combination formula: C(n,r) = n!/(r!*(n-r)!)

format long
factorial(40)/(factorial(20)*factorial(20))
