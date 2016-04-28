class Integer
	def reversable?
		if self%10 == 0
			return false
		else
			return true
		end
	end

	def reverse
		self.to_s.chars.reverse.join.to_i
	end

	def lychrel
		return (self+self.reverse)
	end

	def is_palindrome?
		num_arr = self.to_s
		return num_arr == num_arr.reverse
	end
end

def lychrel_numbers(thresh,max_iter)
	number = 0
	(1..thresh).each do |n|
		counter = max_iter
		while counter > 0
			n = n.lychrel
			if n.is_palindrome?
				break
			end
			counter -= 1
		end
		if counter == 0
			number += 1
		end
	end
	return number
end

start = Time.now
puts lychrel_numbers(10000,50)
puts Time.now-start
