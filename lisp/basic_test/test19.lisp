(defun read-number ()
  (format t "Enter a number: ")
  (finish-output)
  (parse-integer (read-line)))

(defun read-and-sum ()
  (let ((sum 0))
    (do ((i (read-number) (read-number))) ((= i 0) sum)
      (incf sum i))
    (format t "The sum is ~D.~%" sum)))

(read-and-sum)
