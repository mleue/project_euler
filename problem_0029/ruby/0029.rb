powers = Hash.new
(2..100).each do |a|
	(2..100).each do |b|
		powers[[a,b]] = a**b
	end
end

p powers.values.uniq.length
