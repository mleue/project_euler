require 'prime'

class Array
	def is_substring_divisible(divisible_by)
		divisible_by.each do |key,value|
			if self[key[0]..key[1]].join.to_i%value != 0
				return false
			end
		end
		return true
	end
end

def create_divisible_by_hash(thresh)
	divisible_by = Hash.new
	primes = Prime.first thresh
	(1..thresh).each do |n|
		divisible_by[[n,n+2]] = primes[n-1]
	end
	return divisible_by
end

def substring_divisibility
	divisible_by = create_divisible_by_hash(7)
	numbers = [0,1,2,3,4,5,6,7,8,9].permutation.reject{|perm| perm[0] == 0}.to_a
	sum = 0
	numbers.each do |n|
		if n.is_substring_divisible(divisible_by)
			sum += n.join.to_i
		end
	end
	return sum
end

start = Time.now
puts "The sum of all the substring divisible 0-9 pandigital numbers is #{substring_divisibility}"
puts Time.now-start
