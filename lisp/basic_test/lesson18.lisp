(define-condition negative-number (error)
    ((text :initarg :text :reader negative-number-text)))

(defun factorial-4 (n)
    (restart-case
        (cond ((< n 0 ) (error 'negative-number
                               :text "Negative number"))
            ((= n 0) 1)
            (t (* n (factorial-4 (1- n)))))
        (use-abs-value () (- (factorial-4 (- n)))))) 

(defun main-4 (n)
    (handler-bind ((negative-number
                    #'(lambda (c)
                        (declare (ignore c))
                        (invoke-restart 'use-abs-value)))))
    (format t "The factorial is ~A~%" (factorial-4 n)))

(main-4 -5)
