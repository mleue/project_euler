class Integer
	def to_base2
		digits = Math.log2(self).floor
		base2 = 0
		rest = self
		(0..digits).reverse_each do |d|
			current = 2**d
			base2 *= 10
			if current > rest
				next
			end
			rest = rest%current
			base2 += 1
		end
		return base2
	end

	def is_palindrome?
		num_arr = self.to_s
		return num_arr == num_arr.reverse
	end
end

def double_base_palindromes(thresh)
	occurences = []
	(1..thresh).each do |n|
		if n.is_palindrome? && n.to_base2.is_palindrome?
			occurences.push(n)
		end
	end
	return occurences
end

start = Time.now
p double_base_palindromes(1000000).inject(:+)
puts Time.now-start
