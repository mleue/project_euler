require_relative '../0050.rb'

RSpec.describe Array, '#cumsum' do
	context 'for an array of integers' do
		it 'returns the array of the cumulative sum' do
			expect([1,2,3,4,5].cumsum).to eq [1,3,6,10,15]
		end
	end
end

RSpec.describe 'consecutive_prime_sum' do
	context 'for a threshold input' do
		it 'return the highest prime below that threshold that can be described as the sum of consecutive primes' do
			expect(consecutive_prime_sum(100)).to eq 41
			expect(consecutive_prime_sum(1000)).to eq 953
		end
	end
end
