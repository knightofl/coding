(defpackage :tetris
  (:use :common-lisp))

(in-package :tetris)

;;; 게임 보드 설정
(defparameter *board-width* 10)
(defparameter *board-height* 20)
(defparameter *board* (make-array (list *board-height* *board-width*)
                                   :initial-element #\space))

;;; 테트로미노 정의
(defparameter *tetrominoes*
  '((I ((0 1) (1 1) (2 1) (3 1)))
    (O ((0 0) (0 1) (1 0) (1 1)))
    (T ((0 1) (1 0) (1 1) (1 2)))
    (L ((0 2) (1 0) (1 1) (1 2)))
    (J ((0 0) (1 0) (1 1) (1 2)))
    (S ((0 1) (0 2) (1 0) (1 1)))
    (Z ((0 0) (0 1) (1 1) (1 2)))))

;;; 보드 출력 함수
(defun print-board ()
  (dotimes (y *board-height*)
    (dotimes (x *board-width*)
      (format t "~A" (aref *board* y x)))
    (format t "~%")))

(print-board)