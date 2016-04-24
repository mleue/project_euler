require 'prime'

class Array
	def cumsum
		sum = 0
		self.map{|n| sum += n}
	end

	def prime_concumsum_max(limit)
		max = 0
		ret = []
		self.cumsum.reject{|n| n > limit}.each_with_index do |n,i|
			if n.prime?
				max = max > (i+1) ? max : (i+1)
				ret = [n, max]
			end
		end
		return ret
	end
end

def consecutive_prime_sum(limit)
	primes = Prime.each(limit/20).to_a
	max_consecutive_primes = []
	while !primes.empty?
		max_consecutive_primes.push(primes.prime_concumsum_max(limit))
		primes.shift
	end
	return max_consecutive_primes.max_by{|e| e[1]}
end

start = Time.now
limit = 1000000
p consecutive_prime_sum(limit)
puts Time.now-start
