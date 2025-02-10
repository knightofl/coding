(defun sign (n)
    (if (< n 0)
        "negative"
        (if (> n 0)
            "positive"
            "zero")))

(format t "~A~%" (sign 0))

(defun print-sign-1 (n)
    (if (< n 0)
        (format t "negative~%")
        (format t "positive or zeo~%")))

(defun print-sign-2 (n)
    (format t (if (< n 0)
        "negative~%"
        "positive or zero~%")))


(defun print-sign-3 (n)
    (format t "~A~%" (if (< n 0)
        "negative"
        "positive or zero")))

(defun print-sign-4 (n)
    (format t "~A~%" (if (< n 0)
        "negative"
        (if (> n 0)
            "positive"
            "zero"))))