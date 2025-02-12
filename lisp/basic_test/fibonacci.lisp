;; fibonacci

(defun fibo (n)
    (if (<= n 2)
    1
    (+ (fibo (- n 2)) (fibo (1- n)))))

(disassemble 'fibo)


(defun fibo-tr (n &optional (a 0) (b 1))
    (if (= n 0)
    a
    (fibo-tr (- n 1) b (+ a b))))

(disassemble 'fibo-tr)


(defun fibo-tr-opt (n &optional (a 0) (b 1))
    (declare (optimize (speed 3) (safety 0) (debug 0)))
    (if (= n 0)
    a
    (fibo-tr-opt (- n 1) b (+ a b))))

(disassemble 'fibo-tr-opt)


(loop for i from 1 to 10
    do (format t "~D, " (fibo-tr-opt i))
    finally (format t "...~%"))
