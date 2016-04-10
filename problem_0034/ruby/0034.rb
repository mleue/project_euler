class Integer
	def fact
		(1..self).reduce(:*) || 1
	end
end

factorials = (0..9).map(&:fact)

def digit_factorials(factorials)
	(3...3000000).each do |n|
		if n.to_s.chars.map(&:to_i).map{|n| factorials[n]}.inject(:+) == n
			puts n
		end
	end
end

start = Time.now
digit_factorials(factorials)
puts Time.now - start

#for every digit, there is a max of fact(9) ~ 350k added to the final sum
#therefore we only have to check the numbers until about 3mio
