(defpackage :text-tetris
  (:use :common-lisp))

(in-package :text-tetris)

;;; 테트리스 기본 설정
(defparameter *board-width* 10)
(defparameter *board-height* 20)
(defparameter *board* (make-array (list *board-height* *board-width*) :initial-element #\Space))

(defparameter *tetrominoes*
  '(((0 0) (1 0) (0 1) (1 1))   ;; O 블록
    ((0 0) (0 1) (0 2) (0 3))   ;; I 블록
    ((0 0) (1 0) (2 0) (1 1))   ;; T 블록
    ((0 0) (1 0) (1 1) (2 1))   ;; S 블록
    ((0 1) (1 1) (1 0) (2 0))   ;; Z 블록
    ((0 0) (0 1) (0 2) (1 2))   ;; L 블록
    ((0 2) (1 2) (1 1) (1 0)))) ;; J 블록

(defparameter *current-piece* nil)
(defparameter *piece-x* 0)
(defparameter *piece-y* 0)

(defun random-piece ()
  (nth (random (length *tetrominoes*)) *tetrominoes*))

(defun spawn-piece ()
  (setf *current-piece* (random-piece))
  (setf *piece-x* (/ *board-width* 2))
  (setf *piece-y* 0))

(defun can-move-piece (dx dy)
  "블록이 주어진 dx, dy 방향으로 이동 가능한지 검사."
  (every (lambda (block)
           (let* ((new-x (+ *piece-x* (first block) dx))
                  (new-y (+ *piece-y* (second block) dy)))
             (and (>= new-x 0) (< new-x *board-width*)
                  (>= new-y 0) (< new-y *board-height*)
                  (char= (aref *board* new-y new-x) #\Space))))
         *current-piece*))

(defun move-piece (dx dy)
  "블록을 이동."
  (when (can-move-piece dx dy)
    (incf *piece-x* dx)
    (incf *piece-y* dy)
    t))

(defun lock-piece ()
  "블록을 보드에 고정."
  (dolist (block *current-piece*)
    (setf (aref *board* (+ *piece-y* (second block))
                        (+ *piece-x* (first block)))
          #\#))
  (spawn-piece))

(defun update-game ()
  "한 틱마다 블록을 한 칸 아래로 이동."
  (if (move-piece 0 1)
      nil
      (lock-piece)))

(defun print-board ()
  "현재 보드를 출력."
  (loop for y from 0 below *board-height* do
    (loop for x from 0 below *board-width* do
      (let ((occupied (find (list (- x *piece-x*) (- y *piece-y*)) *current-piece* :test #'equal)))
        (format t "~C" (if occupied #\# (aref *board* y x)))))
    (format t "~%")))

(defun game-loop ()
  "간단한 게임 루프."
  (spawn-piece)
  (loop for i from 1 to 20 do  ;; 20 프레임 실행 (테스트용)
    (print-board)
    (update-game)
    (sleep 0.5)  ;; 간단한 딜레이
    (clear-screen)))

(defun clear-screen ()
  "터미널 화면을 클리어."
  (format t "~c[2J~c[H" #\ESC #\ESC))

;;; 실행
(game-loop)