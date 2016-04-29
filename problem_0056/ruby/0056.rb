class Integer
	def digit_sum
		return self.to_s.chars.map(&:to_i).inject(:+)
	end
end

def powerful_digit_sum(thresh)
	max = 0
	(1...thresh).each do |a|
		(1...thresh).each do |b|
			curr = (a**b).digit_sum
			max = max > curr ? max : curr
		end
	end
	return max
end

start = Time.now
puts powerful_digit_sum(100)
puts Time.now-start
