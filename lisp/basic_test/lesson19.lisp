(loop for i below 10 sum i)

(loop for i from 1 to 10 sum i)

(loop for i from 1 to 10 by 2 sum i)

(do ((i 1 (+ i 2))
    (sum 0 (+ sum i)))
    ((> i 10) sum))

(loop for i from 0 to 10 by 2 collect i)

(loop for i from 0 to 10 by 2
    do (print i))

(loop for v in '(a b c d e)
    do (print v))

(loop for v in '(a b c d e)
    for i below 10
    do (format t "~%~A ~A" i v))

(loop for i below 10
    do (loop for v in '(a b c d e)
           do (format t "~%~A ~A" i v)))

(loop for i below 10
    collect (loop for v in '(a b c d e)
           collect (cons i v)))

(loop for i below 10
    nconcing (loop for v in '(a b c d e)
           collect (cons i v)))

(loop for i from 20
    for v in '(a b c d e)
    collect (cons i v))

(loop for i from 20
    for v in '(a b c d e)
    collect (cons i v)
    do (print i))

(loop for (a b) in '((a 1) (b 2) (c 3))
    collect (cons a b))