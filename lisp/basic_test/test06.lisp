;; factorial

(defun fac (n)
    (if (<= n 0)
    1
    (* n (fac (1- n)))))

(loop for i from 1 to 10
    do (format t "~D, " (fac i))
    finally (format t "...~%"))
