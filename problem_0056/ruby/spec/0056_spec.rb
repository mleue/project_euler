require_relative '../0056.rb'

RSpec.describe Integer, '#digit_sum' do
	context 'for an integer input' do
		it 'returns the sum of the digits' do
			expect(123.digit_sum).to eq 6
		end
	end
end
