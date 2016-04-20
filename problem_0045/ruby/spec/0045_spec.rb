require_relative '../0045.rb'

RSpec.describe Integer, '#triangle_number' do
	context 'for an Integer' do
		it 'returns its triangle number value' do
			expect(3.triangle_number).to eq 6
			expect(5.triangle_number).to eq 15
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

RSpec.describe Integer, '#is_triangle_number?' do
	context 'for an Integer' do
		it 'returns whether it is a triangle number' do
			expect(3.is_triangle_number?).to eq true
			expect(6.is_triangle_number?).to eq true
			expect(10.is_triangle_number?).to eq true
			expect(15.is_triangle_number?).to eq true
			expect(12.is_triangle_number?).to eq false
		end
	end
end

RSpec.describe Integer, '#is_hexagonal_number?' do
	context 'for an Integer' do
		it 'returns whether it is a hexagonal number' do
			expect(1.is_hexagonal_number?).to eq true
			expect(6.is_hexagonal_number?).to eq true
			expect(15.is_hexagonal_number?).to eq true
			expect(28.is_hexagonal_number?).to eq true
			expect(45.is_hexagonal_number?).to eq true
			expect(30.is_hexagonal_number?).to eq false
			expect(10.is_hexagonal_number?).to eq false
		end
	end
end

RSpec.describe Integer, '#find_next_tri_pent_hex_number' do
	context 'for an Integer seed' do
		it 'find the next triangle number that is also pentagonal and hexagonal' do
			expect(2.find_next_tri_pent_hex_number).to eq 40755
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
