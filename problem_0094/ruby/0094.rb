#TODO slooooooow
require 'bigdecimal'

def is_integer?(number)
	number%1 == 0
end

def equal_sided_triangle_area(a,c)
	#area = (1.0/2 * Math.sqrt(a**2 - c**2/4.0) * c)
	div = BigDecimal.new('4.0')
	area = Math.sqrt(a**2 - c**2/div)
	return area
end

def almost_equilateral_triangles(thresh)
	occurences = []
	n = 5
	while n < thresh
		number = BigDecimal.new(n.to_s)
		numberp1 = BigDecimal.new((n+1).to_s)
		if is_integer?(equal_sided_triangle_area(number,numberp1))
			occurences.push([n,n,n+1])
			temp = n
			n *= 12
			n -= temp
			next
		end
		n += 2
	end

	n = 3
	while n < thresh
		number = BigDecimal.new(n.to_s)
		numberm1 = BigDecimal.new((n-1).to_s)
		if is_integer?(equal_sided_triangle_area(number,numberm1))
			occurences.push([n,n,n-1])
			temp = n
			n *= 12
			n -= temp
			next
		end
		n += 2
	end
	
	return occurences
end

start = Time.now
occurences = almost_equilateral_triangles(333333333)
p occurences
p occurences.length
p occurences.flatten.inject(:+)
puts Time.now-start
