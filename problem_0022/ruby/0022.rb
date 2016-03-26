def alphabetical_value(name)
	name = name.downcase
	value = 0
	name.each_char do |c|
		value += (c.ord() - 'a'.ord() + 1)
	end
	value
end

names = File.read("../names.txt").split(",").map{|s| s.tr('\"', '')}.sort_by{|name| name.downcase}

namescore = 0
names.each_with_index do |item, index|
	namescore += alphabetical_value(item)*(index+1)
end

puts namescore
