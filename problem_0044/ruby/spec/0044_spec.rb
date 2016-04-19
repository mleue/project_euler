require_relative '../0044.rb'

RSpec.describe Integer, '#pentagonal' do
	context 'for an Integer' do
		it 'returns its pentagonal value' do
			expect(1.pentagonal).to eq 1
			expect(2.pentagonal).to eq 5
			expect(10.pentagonal).to eq 145
		end
	end
end

RSpec.describe Integer, '#is_pentagonal_number?' do
	context 'for an Integer' do
		it 'returns whether it is a pentagonal number' do
			expect(5.is_pentagonal_number?).to eq true
			expect(10.is_pentagonal_number?).to eq false
		end
	end
end

RSpec.describe Float, '#is_int?' do
	context 'for a float input' do
		it 'checks whether it could be described as an int without loss' do
			expect(5.0.is_int?).to eq true
			expect(5.5.is_int?).to eq false
		end
	end
end

RSpec.describe 'create_pentagonal_numbers' do
	context 'for an input of how many elements of the sequence are to be computed' do
		it 'returns an array with the n first elements of the pentagonal sequence' do
			expect(create_pentagonal_numbers(10)).to eq [1, 5, 12, 22, 35, 51, 70, 92, 117, 145]
		end
	end
end
