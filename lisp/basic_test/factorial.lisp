;; factorial

(defun fac (n)
    (if (<= n 0)
    1
    (* n (fac (1- n)))))

(disassemble 'fac)


(defun fac-tr (n &optional (acc 1))
    (if (<= n 0)
    acc
    (fac-tr (- n 1) (* n acc))))

(disassemble 'fac-tr)


(defun fac-tr-opt (n &optional (acc 1))
    (declare (optimize (speed 3) (safety 0) (debug 0)))
    (if (<= n 0)
    acc
    (fac-tr-opt (- n 1) (* n acc))))


(disassemble 'fac-tr-opt)


(loop for i from 1 to 10
    do (format t "~D, " (fac-tr-opt i))
    finally (format t "...~%"))
