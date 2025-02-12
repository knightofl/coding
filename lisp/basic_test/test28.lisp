(defmacro for ((var from to) &rest body)
    (let ((sym-to (gensym)))
        `(do ((,var ,from (1+ ,var))
              (,sym-to ,to))
             ((> ,var ,sym-to))
             ,@body)))

(defmacro for2 ((var from to) &rest body)
    `(do ((,var ,from (1+ ,var))
          (limit ,to))
         ((>= ,var limit))
         ,@body))

(for (i 0 10) (princ i))
