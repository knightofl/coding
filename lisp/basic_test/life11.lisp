(load "~/quicklisp/setup.lisp")
(ql:quickload "sdl2")

(defpackage :game-of-life
  (:use :common-lisp :sdl2))

(in-package :game-of-life)

;; 창 크기와 격자 설정
(defparameter *cell-size* 10)  ;; 셀 한칸의 크기, 픽셀 단위.
(defparameter *rows* 50)       ;; 격자의 행수
(defparameter *cols* 50)       ;; 격자의 열수
(defparameter *window-width* (* *cols* *cell-size*))  ;; 창의 너비
(defparameter *window-height* (* *rows* *cell-size*)) ;; 창의 높이

;; sdl 윈도우 및 렌더러
(defparameter *window* nil)
(defparameter *renderer* nil)

;; sdl 초기화
(defun init-sdl ()
  (sdl2:init :video)
  (setf *window* (sdl2:create-window :title "Game of Life"
                                     :x #x2FFF0000
                                     :y #x2FFF0000
                                     :w *window-width*
                                     :h *window-height*
                                     :flags '(:shown)))
  (setf *renderer* (sdl2:create-renderer *window* -1 '(:accelerated)))
  (sdl2:set-render-draw-color *renderer* 0 0 0 255)
  (sdl2:render-clear *renderer*)
  (sdl2:render-present *renderer*))

(defun quit-sdl ()
  (sdl2:destroy-renderer *renderer*)
  (sdl2:destroy-window *window*)
  (sdl2:quit))

;; 격자 생성
(defun make-grid ()
  (make-array (list *rows* *cols*) :element-type '(integer 0 1) :initial-element 0))

(defun randomize-grid (grid)
  (loop for i below *rows*
       do (loop for j below *cols*
                do (setf (aref grid i j) (if (< (random 1.0) 0.3) 1 0)))))

(defun count-neighbors (grid x y)
  (let ((count 0))
    (loop for dx in '(-1 -1 -1  0  0  1  1  1)
          for dy in '(-1  0  1 -1  1 -1  0  1)
          do (let ((nx (+ x dx))
                   (ny (+ y dy)))
                (when (and (>= nx 0) (< nx *rows*)
                           (>= ny 0) (< ny *cols*))
                    (incf count (aref grid nx ny)))))
    count))

(defun next-generation (grid)
  (let ((new-grid (make-grid)))
    (loop for i below *rows*
          do (loop for j below *cols*
                   do (let ((alive (aref grid i j))
                            (neighbors (count-neighbors grid i j)))
                        (setf (aref new-grid i j)
                              (if (or (and (= alive 1) (or (= neighbors 2) (= neighbors 3)))
                                      (and (= alive 0) (= neighbors 3)))
                                  1
                                  0)))))
    new-grid))

(defun draw-grid (grid)
  (sdl2:set-render-draw-color *renderer* 0 0 0 255) ;; 검은색 배경
  (sdl2:render-clear *renderer*)
  (sdl2:set-render-draw-color *renderer* 0 255 0 255) ;; 초록색 셀
  (loop for i below *rows*
     do (loop for j below *cols*
              do (when (= (aref grid i j) 1)
                (let ((rect (sdl2:make-rect (* j *cell-size*)
                                            (* i *cell-size*)
                                            *cell-size*
                                            *cell-size*)))
                  (sdl2:render-fill-rect *renderer* rect)))))
  (sdl2:render-present *renderer*))

(defun run-life (steps)
  (init-sdl)
  (let ((grid (make-grid)))
    (randomize-grid grid)
    (loop repeat steps
       do (progn
            (draw-grid grid)
            (setf grid (next-generation grid))
            (sdl2:delay 100))))
    (quit-sdl))

(run-life 1000)