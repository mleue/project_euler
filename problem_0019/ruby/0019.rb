require 'date'

from = Date.new(1901, 1, 1)
to = Date.new(2000, 12, 31)

sunday_first_of_month_count = 0
(from..to).each do |day|
	if (day.sunday? && day.day == 1)
		sunday_first_of_month_count += 1
	end
end

puts "There were #{sunday_first_of_month_count} sundays on the first of a month from #{from} to #{to}"
