require 'humanize'

letterSum = 0
for i in 1..1000
	letterSum += i.humanize().tr(' -','').length()
end

puts "The sum of all letters in the numbers from 1 to 1000 written out in words is #{letterSum}"
