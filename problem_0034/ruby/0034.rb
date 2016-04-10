class Integer
	def fact
		(1..self).reduce(:*) || 1
	end
end

def digit_factorials
	(3...3000000).each do |n|
		if n.to_s.chars.map(&:to_i).map(&:fact).inject(:+) == n
			puts n
		end
	end
end

start = Time.now
digit_factorials()
puts Time.now - start
