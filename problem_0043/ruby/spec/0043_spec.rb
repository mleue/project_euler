require_relative '../0043.rb'

divisible_by = create_divisible_by_hash(7)

RSpec.describe Array, '#is_substring_divisible' do
	context "for an array of integers" do
		it "checks if the sliding window subintegers are divisible by the given divisors" do
		expect([1,4,0,6,3,5,7,2,8,9].is_substring_divisible(divisible_by)).to eq true
		expect([1,4,0,5,3,5,7,2,8,9].is_substring_divisible(divisible_by)).to eq false
		end
	end
end
