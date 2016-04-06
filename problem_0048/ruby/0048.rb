def self_powers(thresh)
	sum = 0
	(1..thresh).each do |n|
		sum += n**n
	end
	return sum
end

start = Time.now
puts self_powers(1000)
puts Time.now-start
