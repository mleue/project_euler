class Float
	def is_int?
		if self%1 == 0
			return true
		else
			return false
		end
	end
end

perimeters = Hash.new(0)
(2..500).each do |c|
	(1..c-1).each do |a|
		a = a.to_f
		c = c.to_f
		b = Math.sqrt(c**2-a**2)
		p = a+b+c
		if b.is_int? && p <= 1000
			perimeters[p] += 1
		end
	end
end
p perimeters.max_by{|k,v| v}
