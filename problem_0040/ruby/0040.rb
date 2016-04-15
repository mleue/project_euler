start = Time.now
def digit_product(digits)
	number =  (0..200000).to_a.join
	product = 1
	digits.each do |digit|
		product *= number[digit].to_i
	end
	return product
end
digits = (0..6).map{|n| 10**n}
product = digit_product(digits)
puts "The product of the digits #{digits} is #{product}"
puts Time.now-start
