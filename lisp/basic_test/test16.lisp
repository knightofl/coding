(defun read-number ()
    (format t "Enter a number: ")
    (finish-output)
    (parse-integer (read-line)))

(defun add-numbers ()
    (let ((sum 0))
        (do ((i (read-number) (read-number)))
            ((= i 0) (format t "The sum is ~D~%" sum) sum)
            (setf sum (+ sum i)))))

(add-numbers)