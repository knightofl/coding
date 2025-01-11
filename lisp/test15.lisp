(defun read-number ()
    (format t "Enter a number: ")
    (finish-output)
    (parse-intger (read-line)))

(defun add-numbers (n)
    (let ((sum  0))
        (dotimes (i n)
            (setf sum (+ sum (read-number))))
        (format t "The sum is ~D~%" sum)
        sum))

(add-numbers 3)