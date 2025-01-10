(defun ask-and-return-name ()
  (format t "What is your name? ")
  (finish-output)
  (let ((name (read-line)))
    (format t "Hello, ~A!~%" name)
    name))

;;(ask-and-return-name)
(princ (ask-and-return-name))