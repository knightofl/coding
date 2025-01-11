(defun ask-name ()
    (format t "What is your name? ")
    (finish-output)
    (read-line))

(defun return-name ()
    (let ((name (ask-name)))
         (format t "Hello, ~A!~%" name)
         name))
 
(return-name)
;;(princ (return-name))
