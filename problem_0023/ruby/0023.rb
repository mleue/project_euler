require_relative 'lib/fixnum_ext.rb'

time_begin = Time.now
thresh = 28123
abundant_numbers = []
(1...thresh).each do |n|
	if (n.abundant?)
		abundant_numbers.push(n)
	end
end

#sum up all the 2-element subsets of the abundant numbers and delete all duplicates and all under the threshold
sums_of_abundant_numbers = abundant_numbers.combination(2).to_a.map{|arr| arr.inject(:+)}.push(abundant_numbers.map{|n| n*2}).flatten.uniq.delete_if{|sum| sum > thresh}
#what numbers below the threshold can therefore not be computed as the sum of two abundant numbers?
p ((1...thresh).to_a - sums_of_abundant_numbers).inject(:+)
puts Time.now-time_begin
