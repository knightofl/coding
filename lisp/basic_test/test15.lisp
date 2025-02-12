(defun read-number ()
    (format t "Enter a number: ")
    (finish-output)
    (parse-integer (read-line)))

(defun add-numbers (n)
    (let ((sum  0))
        (dotimes (i n)
            (format t "~D." i)
            (setf sum (+ sum (read-number)))) ; (incf sum (read-number))
        (format t "The sum is ~D~%" sum)
        sum))

;(add-numbers 5)

(defun add-numbers-2 (n)
    (let ((sum  0))
        (do ((i 0 (1+ i)))
            ((= i n) (format t "The sum is ~D~%" sum) sum)
            (format t "~D." i)
            (setf sum (+ sum (read-number))))))

(add-numbers-2 5)