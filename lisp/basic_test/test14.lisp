(defun read-number ()
    (format t "Enter a number: ")
    (finish-output)
    (parse-intger (read-line)))

(princ (read-number))

         