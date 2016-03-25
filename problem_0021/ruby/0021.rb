def divisorSum(number)
	sum = 0
	(1..number/2).each do |n|
		sum += number%n == 0 ? n : 0
	end
	sum
end

underX = 10000;

#calculate the sum of proper divisors for the given range
divisor_sums = Hash.new()
(1...underX).each do |n|
	divisor_sums[n] = divisorSum(n)
end

#find all amicable numbers
amicables = Array.new()
(1...underX).each do |n|
	if (n == divisor_sums[divisor_sums[n]] && n != divisor_sums[n])
		amicables.push(divisor_sums[n])
	end
end

puts amicables.inject(:+)
