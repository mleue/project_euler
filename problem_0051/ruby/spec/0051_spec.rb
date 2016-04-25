require_relative '../0051.rb'

RSpec.describe Array, '#contains_duplicate?' do
	context 'for an array' do
		it 'checks whether there is any duplicate element and returns an array with them if yes' do
			expect(["A", "B", "C", "B", "A"].contains_duplicate?).to eq ["A", "B"]
			expect(["A", "B", "C"].contains_duplicate?).to eq false
		end
	end
end

RSpec.describe Array, '#replace_element_by' do
	context 'on an array when inputing a certain element and what to replace it with' do
		it 'replaces all occurences of that element with the replacement' do
			expect(["A", "B", "C", "A", "A"].replace_element_by("A","Z")).to eq ["Z", "B", "C", "Z", "Z"]
		end
	end
end
