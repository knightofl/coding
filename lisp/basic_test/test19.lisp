(defun exprbis (&rest x)
    `(+ 2 (* 3 ,@x))) ; backquote

(format t "~S" (exprbis 4 5 6))
