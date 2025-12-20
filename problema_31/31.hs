valores = [1,2,5,10,20,50,100,200]

euler_31 :: Integer -> Integer

euler_31 valor
    | valor <= 0 = 0
    | otherwise = rec_coin (reverse [v | v <- valores, v <= valor]) valor

rec_coin :: [Integer] -> Integer -> Integer

rec_coin [] _ = 0
rec_coin _ 0 = 0
rec_coin _ 1 = 1

rec_coin (candidato:pila) valor
    | candidato == 1 = 1
    | valor - candidato > 0 && candidato > valor - candidato = rec_coin pila (valor-candidato) + rec_coin pila valor
    | valor - candidato > 0 = rec_coin (candidato:pila) (valor-candidato) + rec_coin pila valor
    | valor - candidato == 0 = 1 + rec_coin (pila) valor
