#revised, faster solution after reading:
#http://www.mathblog.dk/project-euler-26-find-the-value-of-d-1000-for-which-1d-contains-the-longest-recurring-cycle/

sequence_length = 0
position = 0

(1...1000).reverse_each do |i|
	if sequence_length >= i
		break
	end
	remainders = Hash.new(0)
	value = 1
	pos = 0

	while (remainders[value] == 0 && value != 0)
		remainders[value] = pos
		value *= 10
		value %= i
		pos += 1
	end

	if pos-remainders[value] > sequence_length
		sequence_length = pos - remainders[value]
		position = pos
	end
end

puts sequence_length
puts position
