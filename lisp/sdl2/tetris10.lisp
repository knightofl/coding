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

(defun rotate (tetromino)
  (apply #'mapcar #'list (reverse tetromino)))

(defun move (tetromino dx dy)
  (mapcar (lambda (row) (mapcar (lambda (cell) (+ cell dx)) row)) tetromino))

(defun collides-p (board tetromino x y)
  (some #'identity
        (mapcar (lambda (row dy)
                  (some #'identity
                        (mapcar (lambda (cell dx)
                                  (and (not (zerop cell))
                                       (or (< (+ x dx) 0)
                                           (>= (+ x dx) *width*)
                                           (< (+ y dy) 0)
                                           (>= (+ y dy) *height*)
                                           (not (zerop (aref board (+ y dy) (+ x dx))))))
                                row (loop for i from 0 below (length row) collect i))))
                tetromino (loop for i from 0 below (length tetromino) collect i)))))

(defun fix-tetromino (board tetromino x y)
  (mapcar (lambda (row dy)
            (mapcar (lambda (cell dx)
                      (when (not (zerop cell))
                        (setf (aref board (+ y dy) (+ x dx)) cell)))
                    row (loop for i from 0 below (length row) collect i)))
          tetromino (loop for i from 0 below (length tetromino) collect i)))

(defun clear-lines (board)
  (let ((new-board (make-array (list *height* *width*) :initial-element 0))
        (new-y (1- *height*)))
    (loop for y from (1- *height*) downto 0 do
      (unless (every #'zerop (aref board y))
        (setf (aref new-board new-y) (aref board y))
        (decf new-y)))
    new-board))    

(defun print-board (board)
  (loop for y from 0 below *height* do
    (loop for x from 0 below *width* do
      (format t "~a " (aref board y x)))
    (format t "~%")))

(defun tetris ()
  (let ((current-tetromino (nth (random (length *tetrominoes*)) *tetrominoes*))
        (x (floor (/ *width* 2)))
        (y 0))
    (loop
      (print-board *board*)
      (let ((input (read)))
        (case input
          ('left (unless (collides-p *board* current-tetromino (1- x) y)
                   (decf x)))
          ('right (unless (collides-p *board* current-tetromino (1+ x) y)
                   (incf x)))
          ('rotate (setf current-tetromino (rotate current-tetromino)))
          ('down (if (collides-p *board* current-tetromino x (1+ y))
                     (progn
                       (fix-tetromino *board* current-tetromino x y)
                       (setf *board* (clear-lines *board*))
                     (incf y)))))))))

(tetris)