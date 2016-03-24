class Integer
	def fact
		(1..self).reduce(:*) || 1
	end
end

class Integer
	def digits(base: 10)
		quotient, remainder = divmod(base)
		quotient == 0 ? [remainder] : [*quotient.digits(base: base), remainder]
	end
end

puts 100.fact.digits.inject(:+)
