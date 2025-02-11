(defpackage :tetris
  (:use :common-lisp))

(in-package :tetris)

(defparameter *board-width* 10)
(defparameter *board-height* 20)

(defparameter *shapes*
  '(((0 1) (1 1) (2 1) (3 1))  ; I
    ((1 0) (1 1) (1 2) (2 2))  ; L
    ((1 0) (1 1) (1 2) (0 2))  ; J
    ((0 1) (1 1) (1 2) (2 2))  ; Z
    ((1 1) (2 1) (0 2) (1 2))  ; S
    ((1 1) (0 2) (1 2) (2 2))  ; T
    ((0 1) (1 1) (0 2) (1 2)))) ; O

(defun rotate-shape (shape)
  "블록을 시계 방향으로 90도 회전."
  (let* ((max-x (apply #'max (mapcar #'first shape)))
         (rotated (mapcar (lambda (pos)
                            (destructuring-bind (x y) pos
                              (list (- max-x y) x)))
                          shape)))
    rotated))

(defun test-rotation ()
  (dolist (shape *shapes*)
    (format t "Original: ~a~%" shape)
    (format t "Rotated:  ~a~%~%" (rotate-shape shape))))

(test-rotation)
