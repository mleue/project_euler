class Fixnum
	def abundant?
		self.divisorSum > self
	end

	def divisorSum
		sum = 0
		(1..self/2).each do |i|
			sum += (self%i == 0) ? i : 0
		end
		sum
	end
end

abundant_numbers = []
(1..28123).each do |n|
	if (n.abundant?)
		abundant_numbers.push(n)
	end
end

puts abundant_numbers.length
