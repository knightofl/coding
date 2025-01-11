(defun read-number ()
    (format t "Enter a number: ")
    (finish-output)
    (parse-intger (read-line)))

(defun add-two-numbers ()
    (let ((num1 (read-number))
          (num2 (read-number)))
        (format t "The number is ~D~%" (+ num1 num2))
        (+ num1 num2)))
 
         