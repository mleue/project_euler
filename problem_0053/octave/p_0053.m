combinations = @(n,r) factorial(n)/(factorial(r)*factorial(n-r)); 

tic
counter = 0;
for n=1:100
	for r=1:n
		if combinations(n,r) > 1000000
			counter += 1;
		end
	end
end
counter
toc
