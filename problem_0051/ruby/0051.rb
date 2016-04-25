require 'prime'

class Array
	def contains_duplicate?
		duplicates = self.group_by{ |e| e }.select { |k, v| v.size > 1 }.map(&:first)
		if duplicates.empty?
			return false
		else
			return duplicates
		end
	end

	def replace_element_by(el,by)
		self.map{|e| e == el ? by : e}
	end
end

class Integer
	def prime_replacable?(limit,duplicate)
		number = self.to_s.chars
		counter = 0
		remain = 10
		("0".."9").each do |n|
			checknum = number.replace_element_by(duplicate[0],n)
			if checknum[0] != "0" && checknum.join.to_i.prime?
				counter += 1
			end
			remain -= 1
			if (counter+remain) < limit
				break
			end
		end
		if counter == limit
			return true
		else
			return false
		end
	end
end

def prime_digit_replacements(limit)
	Prime.each(10000000) do |p|
		dup = p.to_s.chars.contains_duplicate?
		if dup
			if p.prime_replacable?(limit,dup)
				return [p, dup]
			end
		end
	end
end

start = Time.now
p prime_digit_replacements(8)
puts Time.now-start
