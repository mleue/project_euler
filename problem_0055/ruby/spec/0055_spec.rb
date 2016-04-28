require_relative '../0055.rb'

RSpec.describe Integer, '#reversable?' do
	context "for an integer" do
		it "returns whether it is reversable" do
			expect(123.reversable?).to eq true
			expect(120.reversable?).to eq false
		end
	end
end

RSpec.describe Integer, '#reverse' do
	context "for an integer" do
		it "returns the reverse value" do
			expect(123.reverse).to eq 321
		end
	end
end

RSpec.describe Integer, '#lychrel' do
	context "for an integer" do
		it "returns the lychrel value" do
			expect(47.lychrel).to eq 121
		end
	end
end

RSpec.describe Integer, "#is_palindrome?" do
	context "for a Fixnum input" do
		it "returns whether the number is a palindrome" do
			expect(585.is_palindrome?).to eq true
			expect(1001001001.is_palindrome?).to eq true
			expect(123.is_palindrome?).to eq false
		end
	end
end
