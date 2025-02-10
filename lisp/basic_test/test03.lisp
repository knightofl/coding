;; 지역변수, 함수

(let ((a 4) (b 5))
    (* a b))

(let* ((a 4) (b (+ a 2)))
    (* a b))

(flet ((f (n)
    (+ 4 n)))
    (f 5))

(flet ((f (n) (* 2 n))
    (g (n) (+ 3 n)))
    (f (g 5)))

(labels ((f (n) (* n 5))
    (g (n) (+ (f n) 6)))
    (g 10))
