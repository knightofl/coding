(defmacro for ((var from to) &rest body)
    `(do ((,var ,from (1+ ,var))
          (limit ,to))
         ((>= ,var limit))
         ,@body))

(defmacro for ((var from to) &rest body)
    (let ((sym-to (gensym)))
        `(do ((,var ,from (1+ ,var))
              (,sym-to ,to))
             ((>= ,var ,sym-to))
             ,@body)))

(for (i 0 10) (princ i))
