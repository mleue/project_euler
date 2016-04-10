def pandigital_products()
	arr = [1,2,3,4,5,6,7,8,9]
	products = []

	(1..9999).each do |i|
		(1..9999).each do |j|
			product = i*j
			if product > 9999
				next
			end
			arr_compare = i.to_s.chars.map(&:to_i) + j.to_s.chars.map(&:to_i) + product.to_s.chars.map(&:to_i)
			if (arr - arr_compare).empty?
				puts "#{i}x#{j} = #{product}"
				products.push(product)
			end
		end
	end

	return products
end

start = Time.now
products = pandigital_products()
puts "The sum of all 1-9 pandigital products is: #{products.uniq.inject(:+)}"
puts Time.now-start
