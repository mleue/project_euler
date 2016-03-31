require_relative 'lib/prime.rb'

thresh = 1000
a_arr = (-thresh...thresh).to_a
#it is sufficient for b_arr to be composed of only primes, because 
#n*n+a*n+b can only be a prime for n=0 if b is a prime
b_arr = remove_non_primes((-thresh...thresh).to_a)

#2 dimensional hash
check = Hash.new
a_arr.each do |a|
	b_arr.each do |b|
		check[[a,b]] = true
	end
end

i = 0
time_begin = Time.now
while true
	puts i
	if check.length == 1
		p check
		break
	end
	check.each_key do |key|
		a = key[0]
		b = key[1]
		current = i*i+a*i+b
		if !is_prime?(current)
			check.delete(key)
		end
	end
	i += 1
end
puts Time.now-time_begin
