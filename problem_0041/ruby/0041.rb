require 'prime.rb'

def pandigital_prime
	i = 9
	while i > 0
		(1..i).to_a.permutation.to_a.reverse_each do |n|
			n = n.join.to_i
			if Prime.prime?(n)
				return n
			end
		end
		i -= 1
	end
end

start = Time.now
puts "The largest n-pandigital prime is #{pandigital_prime}"
puts Time.now-start
