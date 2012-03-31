x = true
y = false

t = { value = 123, text = "hello" }

function foo()
    print("Hello")
end

bar = function() print("First Class") end

--print(t.value)
--print(foo)
--print(type(bar))

ages = {
    mary = 29,
    john = 31,
    louis = 12
}

letters = { "a", "b", "c", "d" }

for name, age in pairs(ages) do
    --print(name, age)
end

for letter in ipairs(letters) do
    --print(letter)
end

function plus()
    local mem = 0
    function f()
        mem = mem + 1
        return mem
    end
    return f
end

do
    local m = 0
    function lol()
        m = m + 1
        return m
    end
end

do
    local a = 0
    local b = 1
    function fibgen()
        a, b = b, a + b
        return a
    end
end

function fibonacci(n)
    if n < 2 then
        return n
    else
        return fibonacci(n - 1) + fibonacci(n - 2)
    end
end

function fibonacci2(n)
    local a = 0
    local b = 1
    for i = 1, n do
        a, b = b, a + b
    end
    return a
end

function fibonacci_generator()
    function build()
        local a = 0
        local b = 1
        function gen()
            a, b = b, a + b
            return a
        end
        return gen
    end
    return build()
end

fgen1 = fibonacci_generator()
fgen2 = fibonacci_generator()
for i = 1, 10 do
    --print(fgen1())
end

function sum1(n)
    local total = 0
    for i = 1, n do
        total = total + i        
    end
    return total
end

function sum2(n)
    if n == 1 then
        return 1
    else
       return n + sum2(n - 1) 
    end
end

for i = 18000, 1, -1 do
    print(sum2(i))
end


