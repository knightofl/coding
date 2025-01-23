(defmacro for ((var from to) &rest body)
    (let ((sym-to (gensym)))
        `(do ((,var ,from (1+ ,var))
              (,sym-to ,to))
             ((> ,var ,sym-to))
             ,@body)))

(for (i 0 10) (princ i))

(for (limit 0 10) (princ limit))