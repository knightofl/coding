(defun print-sign (n)
    (format t "~A~%"
        (cond
            ((< n 0) "negative")
            ((> n 0) "positive")
            (t "zero"))))

(print-sign 0)