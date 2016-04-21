require 'prime'

class Integer
	def is_prime_square_addable?
		Prime.each(self) do |p|
			sum = 0
			i = 1
			while sum<self
				sum = p+2*i**2
				if sum==self
					return true
				end
				i += 1
			end
		end
		return false
	end
end

def goldbach_closure_first_violation
	n = 33
	while true
		if !Prime.prime?(n)
			if !n.is_prime_square_addable?
				return n
			end
		end
		n += 2
	end
end

start = Time.now
puts "The first odd composite number to violate the goldbach closure is #{goldbach_closure_first_violation}"
puts Time.now-start
