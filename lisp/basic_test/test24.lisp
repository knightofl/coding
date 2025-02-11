(defun my-when (condition true-fn)
    (if condition (funcall true-fn)))

(my-when t (lambda () (princ "hello")
                      (princ "world")))

(defmacro my-and (&rest exprs)
    (if (= (length exprs) 1)
        (first exprs)
        `(if ,(first exprs)
             ,(first exprs)
              (my-and ,@(rest exprs)))))