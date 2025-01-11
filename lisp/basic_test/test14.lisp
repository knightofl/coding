(defun read-number ()
    (format t "Enter a number: ")
    (finish-output)
    (parse-integer (read-line)))

(defun add-two-numbers ()
    (let ((num1 (read-number))
          (num2 (read-number)))
        (princ (+ num1 num2))))

(add-two-numbers)
         