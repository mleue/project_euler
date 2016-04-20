class Integer
	def is_pentagonal_number?
		base = (1+Math.sqrt(1+24*self))/6
		return base.is_int?
	end

	def is_triangle_number?
		base = (-1+Math.sqrt(1+8*self))/2
		return base.is_int?
	end

	def is_hexagonal_number?
		base = (1+Math.sqrt(1+8*self))/4
		return base.is_int?
	end

	def triangle_number
		return (self*(self+1))/2
	end

	def find_next_tri_pent_hex_number
		n = self
		while true
			triangle = n.triangle_number
			if (triangle.is_hexagonal_number? && triangle.is_pentagonal_number?)
				return triangle
			end
			n += 1
		end
	end
end

class Float
	def is_int?
		return self%1 == 0
	end
end

start = Time.now
puts "The next triangle number that is also pentagonal and hexagonal after 40755 is #{286.find_next_tri_pent_hex_number}"
puts Time.now-start
