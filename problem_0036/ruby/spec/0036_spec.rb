require_relative '../0036.rb'

RSpec.describe Fixnum, "#to_base2" do
	context "for a base 10 input" do
		it "returns the base 2 representation" do
			expect(585.to_base2).to eq 1001001001
		end
	end
end

RSpec.describe Fixnum, "#is_palindrome?" do
	context "for a Fixnum input" do
		it "returns whether the number is a palindrome" do
			expect(585.is_palindrome?).to eq true
			expect(1001001001.is_palindrome?).to eq true
			expect(123.is_palindrome?).to eq false
		end
	end
end
