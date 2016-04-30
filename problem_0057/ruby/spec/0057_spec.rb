require_relative '../0057.rb'

RSpec.describe Float, '#to_num_den' do
	context 'for a float input' do
		it 'returns an array containing the numerator, denumerator expression of the original float' do
			expect(1.5.to_num_den).to eq [3,2]
			expect(1.4.to_num_den).to eq [7,5]
			expect((17.0/29.0).to_num_den).to eq [17,29]
		end
	end
end
