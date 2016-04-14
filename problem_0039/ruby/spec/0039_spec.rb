require_relative '../0039.rb'

RSpec.describe Float, '#is_int?' do
	context "for a float input" do
		it "returns whether the float can be described as an integer without loss" do
			expect(513.0.is_int?).to eq true
			expect(513.3.is_int?).to eq false
		end
	end
end
