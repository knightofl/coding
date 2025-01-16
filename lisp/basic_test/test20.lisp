;(defun foo (x) 12)
(defmacro foo (x) 12)
(format t "~D~%" (foo x))

(defun plusf (a b) (+ a b))
(format t "~D~%" (plusf 1 2))

(defun plusfb (a b) `(+ ,a ,b))
(format t "~S~%" (plusfb 1 2))

(defmacro plusfm (a b) `(+ ,a ,b))
(format t "~S~%" (macroexpand-1 '(plusfm 1 2)))
