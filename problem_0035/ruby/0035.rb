require 'prime.rb'

def erastothenes(thresh)
	start = (3...thresh).to_a
	i = start[0]
	while i<thresh
		if !Prime.prime?(i)
			start = start - (i..thresh).step(i).to_a
		end
		i += 1
	end
	return start
end

def circular_primes(thresh)
	occurences = 0
	(1...thresh).each do |n|
		n = n.to_s.chars.map(&:to_i)
		prime_rotations = true
		(0...n.length).each do |rotation|
			n = n.rotate
			if !Prime.prime?(n.join.to_i)
				prime_rotations = false
				break
			end
		end
		if prime_rotations
			occurences += 1
		end
	end
	return occurences
end

start = Time.now
puts circular_primes(1000000)
puts Time.now-start
