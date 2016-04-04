start = Time.now
goal = 2.00
coins = [2.00,1.00,0.50,0.20,0.10,0.05,0.02,0.01]

combinations = 0
(0..goal/coins[0]).each do |twoeur|
	sumtwoeur = twoeur*coins[0]
	if sumtwoeur.round(2) > goal
		break
	end
	(0..goal/coins[1]).each do |oneeur|
		sumoneeur = sumtwoeur+oneeur*coins[1]
		if sumoneeur.round(2) > goal
			break
		end
		(0..goal/coins[2]).each do |fiftyct|
			sumfiftyct = sumoneeur+fiftyct*coins[2]
			if sumfiftyct.round(2) > goal
				break
			end
			(0..goal/coins[3]).each do |twentyct|
				sumtwentyct = sumfiftyct+twentyct*coins[3]
				if sumtwentyct.round(2) > goal
					break
				end
				(0..goal/coins[4]).each do |tenct|
					sumtenct = sumtwentyct+tenct*coins[4]
					if sumtenct.round(2) > goal
						break
					end
					(0..goal/coins[5]).each do |fivect|
						sumfivect = sumtenct+fivect*coins[5]
						if sumfivect.round(2) > goal
							break
						end
						(0..goal/coins[6]).each do |twoct|
							sumtwoct = sumfivect+twoct*coins[6]
							if sumtwoct.round(2) > goal
								break
							end
							(0..goal/coins[7]).each do |onect|
								sumonect = sumtwoct+onect*coins[7]
								if sumonect.round(2) > goal
									break
								end
								#combinations += sumonect == goal ? 1 : 0
								if sumonect.round(2) == goal
									combinations += 1
								end
							end
						end
					end
				end
			end
		end
	end
end

puts combinations
p Time.now-start
