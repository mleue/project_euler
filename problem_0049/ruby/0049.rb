require 'prime'

class Integer
	def is_permutation?(int_val)
		n1_arr = self.to_s.chars.map(&:to_i)
		n2_arr = int_val.to_s.chars.map(&:to_i)
		return (n1_arr-n2_arr | n2_arr-n1_arr).empty?
	end
end

start = Time.now
Prime.take_while{|p| p <= 3333}.reject{|p| p < 1000}.each do |p|
	(3000..4000).each do |n|
		check = p
		counter = 0
		numbers = [p]
		(1..2).each do |times|
			check += n
			if (Prime.prime? check) && p.is_permutation?(check)
				counter += 1
				numbers.push(check)
			end
		end
		if counter == 2
			p numbers
		end
	end
end
puts Time.now-start

#todo write better code ;)
