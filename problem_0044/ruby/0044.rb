class Integer
	def pentagonal
		return (self*(3*self-1))/2
	end

	def is_pentagonal_number?
		base = (1+Math.sqrt(1+24*self))/6
		return base.is_int?
	end
end

class Float
	def is_int?
		return self%1 == 0
	end
end

class Array
	def forward_diff
		l = self.length
		(0..l-2).each do |i|
			(i+1..l-1).each do |j|
				add = self[i]+self[j]
				sub = self[j]-self[i]
				if (add.is_pentagonal_number? && sub.is_pentagonal_number?)
					return [add,sub]
				end
			end
		end
		return forward_diff_hash
	end
end

def create_pentagonal_numbers(n)
	pentagonal_numbers = []
	i = 1
	while pentagonal_numbers.length < n
		pentagonal_numbers.push(i.pentagonal)
		i = i+1
	end
	return pentagonal_numbers
end

def lowest_diff_pentagonal_pair(thresh)
	p create_pentagonal_numbers(thresh).forward_diff
end

start = Time.now
lowest_diff_pentagonal_pair(2500)
puts Time.now-start
