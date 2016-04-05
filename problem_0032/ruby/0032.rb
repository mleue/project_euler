arr = [1,2,3,4,5,6,7,8,9]

p arr.permutation(4).to_a.length
p arr.permutation(3).to_a.length
arr.permutation(2).to_a.each do |n|
	puts n.join.to_i
end
