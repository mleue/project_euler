thresh = 100
solution = []

(10...thresh).each do |i|
	(10...thresh).each do |j|
		if i%10 == 0 || j%10 == 0
			next
		end
		num = i.to_s.chars.map(&:to_i)
		den = j.to_s.chars.map(&:to_i)
		new_num = num-den
		new_den = den-num
		unless new_num.empty? || new_den.empty? || new_num.join.to_i == 0 || new_den.join.to_i == 0 || new_num == num || new_den == den
			if new_num.join.to_f/new_den.join.to_f == i.to_f/j.to_f && new_num.join.to_f/new_den.join.to_f < 1
				solution.push([i,j])
			end
		end
	end
end

p solution
