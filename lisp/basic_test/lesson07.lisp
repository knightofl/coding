;; Usage Example
(if-let (x 12)
    (princ x) (princ "got nil"))

;; Implementation
(defmacro if-let ((x x-val) true-expr false-expr)
    `(let ((,x ,x-val))
        (if ,x ,true-expr ,false-expr)))

(defmacro if-let (binding true-expr false-expr)
    `(let (,binding)
        (if ,(car binding) ,true-expr ,false-expr)))

(defmacro if-let ((x x-val) true-expr &optional false-expr)
    `(let ((,x ,x-val))
        (if ,x ,true-expr ,false-expr)))

(defmacro if-let (binding true-expr &optional false-expr)
    `(let (,binding)
        (if ,(car binding) ,true-expr ,false-expr)))