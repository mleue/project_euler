class Fixnum
	def abundant?
		self.divisorSum > self
	end

	def divisorSum
		sum = 0
		(1..self/2).each do |i|
			sum += (self%i == 0) ? i : 0
			if sum > self
				return sum
			end
		end
		sum
	end
end
