power = 5
#9^5 ~ 60k, so for every additional the max number that can be reached grows by 60k
#->it is sufficient to check until ~400k
sum = 0
(2..400000).each do |n|
	if (n.to_s.chars.map(&:to_i).map{|digit| digit**power}.inject(:+) == n)
		sum += n
	end
end

puts sum
