(defun sum-list (l)
    (let ((sum 0))
        (dolist (v l sum)
            (setf sum (+ sum v)))))

(format t "~D~%" (sum-list '(2 3 4 5)))