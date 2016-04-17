class Integer
	def triangle
		return ((1.0/2.0)*self*(self+1)).to_i
	end
end

class String
	def word_value
		return self.chars.map{|c| c.ord-'A'.ord+1}.inject(:+)
	end
end

def coded_triangle_numbers
	words = File.read("../p042_words.txt").split(",").map{|w| w.delete "\""}
	triangle_numbers = (1..25).to_a.map{|n| n.triangle}
	return words.map{|word| (triangle_numbers.include? word.word_value) ? 1 : 0}.inject(:+)
end

start = Time.now
puts "There are #{coded_triangle_numbers} coded triangle numbers in the provided file"
puts Time.now-start
