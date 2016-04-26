class Integer
	def is_permutation?(int_val)
		n1_arr = self.to_s.chars.map(&:to_i)
		n2_arr = int_val.to_s.chars.map(&:to_i)
		return (n1_arr-n2_arr | n2_arr-n1_arr).empty?
	end
end

def permuted_multiples(factors)
	(1..1000000).each do |n|
		counter = 1
		(2..factors).each do |factor|
			if n.is_permutation?(factor*n)
				counter += 1
			else
				break
			end
		end
		if counter == factors
			return n
		end
	end
end

start = Time.now
puts permuted_multiples(6)
puts Time.now-start
