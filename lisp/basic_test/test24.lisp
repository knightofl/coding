(defun my-when (condition true-fn)
    (if condition (funcall true-fn)))

(my-when t (lambda () (princ "hello")
                      (princ "world")))

