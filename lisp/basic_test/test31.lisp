(defun read-number ()
  (format t "Enter a number: ")
  (finish-output)
  (parse-integer (read-line)))

(defun read-and-sum (n)
  (let ((sum 0))
    (dotimes (i n)
      (incf sum (read-number)))
    (format t "The sum is ~D.~%" sum)))

(read-and-sum 3)
