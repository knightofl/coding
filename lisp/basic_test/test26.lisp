(defun foo (a b &optional c)
  (list a b c))

(foo 1 2)
(foo 1 3 3)

(defun foo (a b &optional c d &rest e)
  (list a b c d e))

(defun foo (&optional a b c d &rest e)
  (list a b c d e))

(defun foo (a &rest params)
  (list a params))

(foo 1 2 3)

(defun foo (&key a b c)
  (list a b c))

(foo :c 3)

(defun foo (&key (a 12) b c)
  (list a b c))

(foo :b 2 :c 3)


