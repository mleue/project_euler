class Float
	def to_num_den
		n = 1
		current = self
		while !current.round(5).is_int?
			n += 1
			current = self*n
		end
		return [current.to_i,n]
	end

	def is_int?
		return self%1 == 0
	end
end

def square_root_convergents
	num = 3
	den = 2
	counter = 0
	(1..1000).each do |n|
		counter += num.to_s.chars.length > den.to_s.chars.length ? 1 : 0
		temp = den
		den = num+den
		num = temp+den
	end
	p counter
end

start = Time.now
square_root_convergents
puts Time.now-start
