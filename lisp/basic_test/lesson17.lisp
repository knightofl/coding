(define-condition negative-number (error)
    ((text :initarg :text :reader negative-number-text)))

(defun factorial-3 (n)
    (cond ((< n 0 ) (error 'negative-number
                           :text "Negative number"))
          ((= n 0) 1)
          (t (* n (factorial-3 (1- n))))))

(defun main-31 (n)
    (format t "The factorial is ~A~%" (factorial-3 n)))

;(main-31 -5)

(defun main-32 (n)
    (handler-case
        (format t "The factorial is ~A~%" (factorial-3 n))
        (negative-number (nne) (format t "~A~%" (negative-number-text nne)))))

(main-32 -5)
