require 'prime'

class Integer
	def truncate_left
		length = self.to_s.length
		return self%(10**(length-1))
	end
	def truncate_right
		remainder = self%10
		return (self-remainder)/10
	end
	def is_truncatable_prime?
		current = self
		while current != 0
			if !Prime.prime?(current)
				return false
			end
			current = current.truncate_left
		end

		current = self
		while current != 0
			if !Prime.prime?(current)
				return false
			end
			current = current.truncate_right
		end

		return true
	end
end

start = Time.now
sum = 0
Prime.each(1000000) do |prime|
	if prime.to_i.is_truncatable_prime? && prime > 10
		sum += prime
	end
end
puts sum
puts Time.now - start
