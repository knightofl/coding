(let ((x x-value))
    (if x true-expr false-expr))

(if-let ((x x-value))
    true-expr
    false-expr)

(defmacro if-let (binding true-expr false-expr)
    `(let (,binding)
        (if ,(car binding) ,true-expr ,false-expr)))

(if-swapped condition false-expr true-expr)
(if condition true-expr false-expr)

(defmacro if-swapped (condition false-expr true-expr)
    `(if ,condition ,true-expr ,false-expr))
