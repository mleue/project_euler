class Array
	def is_nine_pandigital?
		if self.length != 9
			return false
		end
		comp = (1..9).to_a
		if !((self-comp) | (comp-self)).empty?
			return false
		end
		return true
	end
end

start = Time.now
(1..9999).each do |n|
	concat = []
	factor = 1
	while concat.length < 9
		concat += (n*factor).to_s.chars.map(&:to_i)
		factor += 1
	end
	if concat.is_nine_pandigital?
		p concat
	end
end
puts Time.now-start
