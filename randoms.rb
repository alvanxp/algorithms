def acumulateRandoms
	acumulateRandom = 0
	total = 1000
	beforeAcumulate = 0
	while acumulateRandom <= total 
		beforeAcumulate = acumulateRandom
		acumulateRandom+= Random.new.rand(1..100)
		puts acumulateRandom
	end
puts beforeAcumulate
end

def generateGUID
	result = ""
	alphabet = Array[1,2,3,4,5,6,7,8,9,0,"A","B","C","D","E","F" ]
	for i in 1..32 
		digit = alphabet.at(Random.new.rand(0..15)).to_s
		result = i == 9 || i==13 ||i==17 ||i==21? result+='-' : result
		result += digit
	end
	puts result
end

generateGUID
