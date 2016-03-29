def next_fibonacci(a,b)
	a+b
end

a = 1
b = 2
c = 0
index = 3
while (c.to_s.length < 1000)
	c = next_fibonacci(a,b)
	a = b
	b = c
	index += 1
end

puts index
