require_relative '../0052.rb'

RSpec.describe Integer, '#is_permutation?' do
	context 'on an integer and an additional integer input' do
		it 'checks whether they are permutations of each other' do
			expect(1487.is_permutation?(4817)).to eq true
			expect(3331.is_permutation?(3931)).to eq false
		end
	end
end

RSpec.describe 'permuted_multiples' do
	context 'for a maximum factor input' do
		it 'returns the number that can be multiplied by every factor up to that maximum factor and be a permutation of itself' do
			expect(permuted_multiples(6)).to eq 142857
		end
	end
end
