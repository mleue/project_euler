require_relative '../0047.rb'

RSpec.describe Integer, '#prime_factor_decomposition' do
	context 'for an integer input' do
		it 'returns an array of its prime factors' do
			expect(645.prime_factor_decomposition).to eq [3,5,43]
			expect(646.prime_factor_decomposition).to eq [2,17,19]
		end
	end
end

RSpec.describe 'first_n_consecutive_numbers_with_n_distinct_prime_factors' do
	context 'for a natural number input n' do
		it 'returns an array of the first n consecutive numbers with n distinct prime factors' do
			expect(first_n_consecutive_numbers_with_n_distinct_prime_factors(2)).to eq [14,15]
		end
	end
end
