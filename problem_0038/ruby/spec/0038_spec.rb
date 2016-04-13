require_relative '../0038.rb'

RSpec.describe Array, '#is_nine_pandigital?' do
	context "for an array of integers input" do
		it "returns whether the content is 9 pandigital" do
			expect(135792468.to_s.chars.map(&:to_i).is_nine_pandigital?).to eq true
			expect(135.to_s.chars.map(&:to_i).is_nine_pandigital?).to eq false
			expect(222444666.to_s.chars.map(&:to_i).is_nine_pandigital?).to eq false
			expect(12345678999.to_s.chars.map(&:to_i).is_nine_pandigital?).to eq false
		end
	end
end
