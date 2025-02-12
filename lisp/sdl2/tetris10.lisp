(load "~/quicklisp/setup.lisp")

(defpackage :tetris
  (:use :common-lisp))

(in-package :tetris)

(defparameter *width* 10)
(defparameter *height* 20)
(defparameter *board* (make-array (list *height* *width*) :initial-element 0))

(defparameter *tetrominoes*
  '(((1 1 1 1))         ; I
    ((1 1) (1 1))       ; O
    ((0 1 0) (1 1 1))   ; T
    ((1 1 0) (0 1 1))   ; Z
    ((0 1 1) (1 1 0))   ; S
    ((1 0 0) (1 1 1))   ; L
    ((0 0 1) (1 1 1)))) ; J

(defun get-input ()
  "비동기 입력 처리"
  (if (find-package "SB-SYS")
      (funcall (intern "READ-CHAR-NO-HANG" "SB-SYS") *standard-input* nil nil)
      nil))

(defun rotate (tetromino)
  "테트로미노를 시계 방향으로 90도 회전"
  (apply #'mapcar #'list (reverse tetromino)))

(defun collides-p (board tetromino x y)
  "블록이 보드와 충돌하는지 확인"
  (loop for row in tetromino
        for dy from 0
        thereis (loop for cell in row
                      for dx from 0
                      thereis (and (not (zerop cell))
                                   (or (< (+ x dx) 0)
                                       (>= (+ x dx) *width*)
                                       (< (+ y dy) 0)
                                       (>= (+ y dy) *height*)
                                       (not (zerop (aref board (+ y dy) (+ x dx)))))))))

(defun fix-tetromino (board tetromino x y)
  "블록을 보드에 고정"
  (loop for row in tetromino
        for dy from 0
        do (loop for cell in row
                 for dx from 0
                 when (not (zerop cell))
                 do (setf (aref board (+ y dy) (+ x dx)) cell))))

(defun clear-lines (board)
  "완성된 줄을 제거하고 보드를 업데이트"
  (let ((new-board (make-array (list *height* *width*) :initial-element 0))
        (new-y (1- *height*)))
    (loop for y from (1- *height*) downto 0 do
      (if (every #'(lambda (x) (not (zerop x))) (loop for x from 0 below *width* collect (aref board y x)))
          (progn
            (format t "Line cleared at y=~A~%" y)) ; 디버깅용 출력
          (progn
            (loop for x from 0 below *width* do
              (setf (aref new-board new-y x) (aref board y x)))
            (decf new-y))))
    new-board))

(defun print-board (board)
  "보드를 출력"
  (format t "~%~A~%" (make-string (* 2 *width*) :initial-element #\-))
  (loop for y from 0 below *height* do
    (loop for x from 0 below *width* do
      (format t "~A " (if (zerop (aref board y x)) "." "#")))
    (format t "~%"))
  (format t "~A~%" (make-string (* 2 *width*) :initial-element #\-)))

(defun tetris ()
  "테트리스 게임 실행"
  (let ((current-tetromino (nth (random (length *tetrominoes*)) *tetrominoes*))
        (x (floor (/ *width* 2)))
        (y 0))
    (loop
      (print-board *board*)
      (format t "Move: left (a), right (d), rotate (w), drop (s), quit (q)~%")
      (let ((input (get-input)))
        (when input
          (case input
            (#\a (unless (collides-p *board* current-tetromino (1- x) y)
                   (decf x)))
            (#\d (unless (collides-p *board* current-tetromino (1+ x) y)
                   (incf x)))
            (#\w (let ((new-tetromino (rotate current-tetromino)))
                   (unless (collides-p *board* new-tetromino x y)
                     (setf current-tetromino new-tetromino))))
            (#\s (if (collides-p *board* current-tetromino x (1+ y))
                     (progn
                       (fix-tetromino *board* current-tetromino x y)
                       (setf *board* (clear-lines *board*))
                       (setf current-tetromino (nth (random (length *tetrominoes*)) *tetrominoes*))
                       (setf x (floor (/ *width* 2)))
                       (setf y 0))
                     (incf y)))
            (#\q (return)))))
      (sleep 0.5))))  ; 블록이 자동으로 내려가도록 설정

;; 실행
(tetris)
