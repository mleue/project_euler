require_relative '../0037.rb'

RSpec.describe Integer, '#truncate_left' do
	context "for an integer input" do
		it "returns the integer with the leftmost digit cut off" do
			expect(585.truncate_left).to eq 85
		end
	end
end

RSpec.describe Integer, '#truncate_right' do
	context "for an integer input" do
		it "returns the integer with the rightmost digit cut off" do
			expect(585.truncate_right).to eq 58
		end
	end
end

RSpec.describe Integer, '#is_truncatable_prime?' do
	context "for an integer input" do
		it "returns whether the integer is a truncatable prime" do
			expect(3797.is_truncatable_prime?).to eq true
			puts sum
		end
	end
end
