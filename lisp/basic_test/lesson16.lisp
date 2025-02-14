(defun factorial-1 (n)
    (if (= n 0) 1
        (* n (factorial-1 (1- n)))))

(defun main-1 (n)
    (format t "The factorial is ~A~%" (factorial-1 n)))

;(main-1 5)
;(main-1 -5)

(defun factorial-2 (n)
    (cond ((< n 0 ) (error "Negative number"))
          ((= n 0) 1)
          (t (* n (factorial-2 (1- n))))))

(defun main-2 (n)
    (format t "The factorial is ~A~%" (factorial-2 n)))

(main-2 -5)
