def is_prime?(number)
	if (number < 2)
		return false
	end
	(2..(number/2).floor).each do |n|
		if (number%n == 0)
			return false
		end
	end
	return true
end

def remove_non_primes(array)
	array.each do |n|
		if !is_prime?(n)
			array = array - [n]
		end
	end
	return array
end
