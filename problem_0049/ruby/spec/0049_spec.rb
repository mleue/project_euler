require_relative '../0049.rb'

RSpec.describe Integer, '#is_permutation?' do
	context 'on an integer and an additional integer input' do
		it 'checks whether they are permutations of each other' do
			expect(1487.is_permutation?(4817)).to eq true
			expect(3331.is_permutation?(3931)).to eq false
		end
	end
end
