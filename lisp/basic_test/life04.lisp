(load "~/quicklisp/setup.lisp")
(ql:quickload "sdl2")

(defpackage :game-of-life
  (:use :common-lisp :sdl2))

(in-package :game-of-life)

;; 창 크기와 격자 설정
(defparameter *width* 800)
(defparameter *height* 600)
(defparameter *cell-size* 5)
(defparameter *grid-width* (/ *width* *cell-size*))
(defparameter *grid-height* (/ *height* *cell-size*))
(defparameter *grid* (make-array (list *grid-width* *grid-height*) :initial-element nil))
(defparameter *running* nil)
(defparameter *paused* nil)
(defparameter *delay* 50)

;; 랜덤으로 격자 채우기
(defun initialize-grid ()
  (loop for x from 0 below *grid-width* do
    (loop for y from 0 below *grid-height* do
      (setf (aref *grid* x y) (if (< (random 1.0) 0.2) t nil)))))

;; 이웃 셀의 수 계산
(defun count-neighbors (x y)
  (let ((count 0))
    (loop for dx from -1 to 1 do
      (loop for dy from -1 to 1 do
        (unless (and (= dx 0) (= dy 0))
          (let ((nx (mod (+ x dx) *grid-width*)) ; 경계 래핑
                (ny (mod (+ y dy) *grid-height*)))
            (when (aref *grid* nx ny)
              (incf count))))))
    count))

;; 다음 상태 계산
(defun next-generation ()
  (let ((new-grid (make-array (list *grid-width* *grid-height*) :initial-element nil)))
    (loop for x from 0 below *grid-width* do
      (loop for y from 0 below *grid-height* do
        (let ((neighbors (count-neighbors x y)))
          (setf (aref new-grid x y)
                (if (aref *grid* x y)
                    (or (= neighbors 2) (= neighbors 3))
                    (= neighbors 3))))))
    (setf *grid* new-grid)))

;; 렌더링
(defun render-grid (renderer)
  (sdl2:set-render-draw-color renderer 0 0 0 255) ; 배경 검정색
  (sdl2:render-clear renderer)
  (sdl2:set-render-draw-color renderer 0 255 0 255) ; 셀 녹색
  (loop for x from 0 below *grid-width* do
    (loop for y from 0 below *grid-height* do
      (when (aref *grid* x y)
        (sdl2:render-fill-rect renderer
                               (sdl2:make-rect (* x *cell-size*) (* y *cell-size*)
                                               *cell-size* *cell-size*)))))
  (sdl2:render-present renderer))

;; 메인 루프
(defun main ()
  (sdl2:with-init (:video)
    (sdl2:with-window (win :title "Conway's Game of Life" :w *width* :h *height*)
      (sdl2:with-renderer (renderer win)
        (initialize-grid)
        (sdl2:with-event-loop (:method :poll)
          (:quit () t)
          (:keydown (:keysym keysym)
            (cond
              ((sdl2:scancode= (sdl2:scancode-value keysym) :scancode-space)
               (setf *paused* (not *paused*))) ; 스페이스바로 일시 정지/재개
              ((sdl2:scancode= (sdl2:scancode-value keysym) :scancode-r)
               (initialize-grid)) ; R 키로 격자 재설정
              ((sdl2:scancode= (sdl2:scancode-value keysym) :scancode-escape)
               (sdl2:push-event :quit)))) ; ESC 키로 종료
          (:idle ()
            (unless *paused*
              (next-generation))
            (render-grid renderer)
            (sdl2:delay *delay*)))))))

(defun run-life ()
  (sdl2:with-init (:video)
    (sdl2:with-window (win :title "Conway's Game of Life" :w *width* :h *height*)
      (sdl2:with-renderer (renderer win)
        (initialize-grid)
        (sdl2:with-event-loop (:method :poll)
          (:quit () t)
          (:keydown (:keysym keysym)
            (cond
              ((sdl2:scancode= (sdl2:scancode-value keysym) :scancode-space)
               (setf *paused* (not *paused*))) ; 스페이스바로 일시 정지/재개
              ((sdl2:scancode= (sdl2:scancode-value keysym) :scancode-r)
               (initialize-grid)) ; R 키로 격자 재설정
              ((sdl2:scancode= (sdl2:scancode-value keysym) :scancode-escape)
               (sdl2:push-event :quit)))) ; ESC 키로 종료
          (:idle ()
            (unless *paused*
              (next-generation))
            (render-grid renderer)
            (sdl2:delay *delay*))))))
  (sb-ext:gc :full t))

(run-life)
