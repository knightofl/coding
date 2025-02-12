(if t (progn (princ "안녕? ") (princ "여러분! ")))

(when t (princ "안녕? ") (princ "여러분! "))

(macroexpand-1 '(when t (princ "안녕? ") (princ "여러분! ")))