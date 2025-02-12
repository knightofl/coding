(defmacro with-run-or-neg (&body body)
    `(handler-case (progn ,@body)
        (error () -1)))

(with-run-or-neg
    (print "hello world!")
    (error "error!"))

(with-run-or-neg
    (print "hello world!")
    0)

(with-run-or-neg
    (error "error!"))
