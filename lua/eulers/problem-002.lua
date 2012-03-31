sum, a, b = 0, 0, 1

while b < 4000000 do
	a, b = b, a + b
	if b % 2 == 0 then
		sum = sum + b
	end
end

print(sum)
