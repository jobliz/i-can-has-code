total = 0

for n = 1, 999 do
    if n % 3 == 0 or n % 5 == 0 then
    	total = total + n 
    end
end

print(total)
