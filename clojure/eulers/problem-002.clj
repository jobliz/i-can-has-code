(def fib-seq (lazy-cat [0 1]
     (map + fib-seq (rest fib-seq))))

(println (reduce +
      (filter even?
            (take-while #(< % 4000000)
                 fib-seq))))
