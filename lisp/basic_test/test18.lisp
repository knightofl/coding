(defun exprq (x)
    (+ 2 (* 3 x)))

; (princ (exprq 4))

(defun exprc (x)
    (cons '+ (cons 2 (cons (cons '* (cons 3 (cons x nil))) nil))))

(format t "~S = ~D~%" (exprc 4) (exprq 4))

(defun exprl (x)
    (list '+ 2 (list '* 3 x)))

(format t "~S = ~D~%" (exprl 4) (exprq 4))