(defun sign (n)
    (cond
        ((< n 0) "negative")
        ((> n 0) "positive")
        (t "zero")))

(format t "~A~%" (sign 0))