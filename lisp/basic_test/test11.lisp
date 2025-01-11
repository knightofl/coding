(defun sign (n)
    (if (< n 0)
        "negative"
        (if (> n 0)
            "positive"
            "zero")))

(format t "~A~%" (sign 0))
