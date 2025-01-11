; fibonacci

(defun fibo (n)
    (if (<= n 2)
    1
    (+ (fibo (- n 2)) (fibo (1- n)))))

(loop for i from 1 to 16
    do (format t "~D, " (fibo i))
    finally (format t "...~%"))