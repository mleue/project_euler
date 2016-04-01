def number_spiral_diags_sum(diag)
	thresh = diag-1
	center = [1]
	diag1 = center.push((1..thresh).map{|n| n*2}).flatten
	diag2 = (1..thresh/2).to_a.concat((1..thresh/2).to_a).map{|n| n*4}.sort

	sum = 0
	cumsum = 0
	diag1.each do |n|
		cumsum += n
		sum += cumsum
	end

	cumsum = 1
	diag2.each do |n|
		cumsum += n
		sum += cumsum
	end

	return sum
end

time_begin = Time.now
p number_spiral_diags_sum(1001)
p Time.now - time_begin
