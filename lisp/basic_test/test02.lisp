;; 전역변수 선언 ex, defvar

(defparameter *big* 100)
(defparameter *small* 1)

(defun guess_my_num()
    (ash (+ *big* *small*) -1))

(defun smaller()
    (setf *big* (1- (guess_my_num)))
    (guess_my_num))

(defun bigger()
    (setf *small* (1+ (guess_my_num)))
    (guess_my_num))

(defun start_over()
    (defparameter *small* 1)
    (defparameter *big* 100)
    (guess_my_num))
