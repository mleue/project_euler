require 'prime'

class Integer
	def prime_factor_decomposition
		rest = self
		factors = []
		while rest != 1
			if Prime.prime? rest
				factors.push(rest)
				break
			end
			Prime.each(rest) do |p|
				if rest%p == 0
					rest /= p
					factors.push(p)
					break
				end
			end
		end
		return factors
	end
end

def first_n_consecutive_numbers_with_n_distinct_prime_factors(n)
	counter = 0
	i = 1
	while counter<n
		if i.prime_factor_decomposition.uniq.length == n
			counter += 1
		else
			counter = 0
		end
		i += 1
	end
	return (1..n).reverse_each.to_a.map{|number| i-number}
end

start=Time.now
p first_n_consecutive_numbers_with_n_distinct_prime_factors(4)
puts Time.now-start
