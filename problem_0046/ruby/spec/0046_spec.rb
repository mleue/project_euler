require_relative '../0046.rb'

RSpec.describe Integer, '#is_prime_square_addable?' do
	context 'for an odd composite integer' do
		it 'checks whether the number can be described as the sum of a prime and twice a square number' do
			expect(9.is_prime_square_addable?).to eq true
			expect(15.is_prime_square_addable?).to eq true
			expect(21.is_prime_square_addable?).to eq true
			expect(25.is_prime_square_addable?).to eq true
			expect(27.is_prime_square_addable?).to eq true
			expect(33.is_prime_square_addable?).to eq true
		end
	end
end
