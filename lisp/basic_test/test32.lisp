(defun read-number ()
  (format t "Enter a number: ")
  (finish-output)
  (parse-integer (read-line)))

(defun read-and-sum (n)
  (let ((sum 0))
    (do ((i 0 (1+ i))) ((= i n) sum)
      (incf sum (read-number)))
    (format t "The sum is ~D.~%" sum)))

(read-and-sum 3)
