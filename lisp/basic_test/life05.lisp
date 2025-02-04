(load "~/quicklisp/setup.lisp")
(ql:quickload "sdl2")

(defpackage :game-of-life
  (:use :common-lisp :sdl2))

(in-package :game-of-life)

(defparameter *width* 800)
(defparameter *height* 600)
(defparameter *cell-size* 10)
(defparameter *grid-width* (/ *width* *cell-size*))
(defparameter *grid-height* (/ *height* *cell-size*))
(defparameter *grid* (make-array (list *grid-width* *grid-height*) :initial-element nil))
(defparameter *paused* t)
(defparameter *pattern-file* "pattern.txt")

;; 격자 초기화 (랜덤 옵션)
(defun initialize-grid (&optional (randomize nil))
  (loop for x from 0 below *grid-width* do
    (loop for y from 0 below *grid-height* do
      (setf (aref *grid* x y) (if randomize (if (< (random 1.0) 0.2) t nil) nil)))))

;; 이웃 계산 (경계 래핑)
(defun count-neighbors (x y)
  (let ((count 0))
    (loop for dx from -1 to 1 do
      (loop for dy from -1 to 1 do
        (unless (and (= dx 0) (= dy 0))
          (let ((nx (mod (+ x dx) *grid-width*))
                (ny (mod (+ y dy) *grid-height*)))
            (when (aref *grid* nx ny)
              (incf count))))))
    count))

;; 다음 세대 계산
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
  (sdl2:set-render-draw-color renderer 0 0 0 255)
  (sdl2:render-clear renderer)
  (sdl2:set-render-draw-color renderer 255 255 255 255)
  (loop for x from 0 below *grid-width* do
    (loop for y from 0 below *grid-height* do
      (when (aref *grid* x y)
        (sdl2:render-fill-rect renderer
                               (sdl2:make-rect (* x *cell-size*) (* y *cell-size*)
                                               *cell-size* *cell-size*)))))
  (sdl2:render-present renderer))

;; 패턴 저장
(defun save-pattern (filename)
  (with-open-file (stream filename :direction :output :if-exists :supersede)
    (loop for y from 0 below *grid-height* do
      (loop for x from 0 below *grid-width* do
        (princ (if (aref *grid* x y) "#" ".") stream))
      (terpri stream))))

;; 패턴 불러오기
(defun load-pattern (filename)
  (when (probe-file filename)
    (initialize-grid nil)
    (with-open-file (stream filename :direction :input)
      (loop for y from 0 below *grid-height*
            for line = (read-line stream nil nil)
            while line do
        (loop for x from 0 below (min (length line) *grid-width*)
              for char = (char line x) do
          (setf (aref *grid* x y) (char= char #\#)))))))





;; 마우스 이벤트 처리 함수 수정
(defun handle-mouse-event (event)
(let ((event-type (sdl2:get-event-type event)))
(when (or (eql event-type :mousebuttondown)
(eql event-type :mousebuttonup))
(let* ((x (sdl2:mouse-button-x event))
(y (sdl2:mouse-button-y event))
(grid-x (floor x *cell-size*))
(grid-y (floor y *cell-size*)))
(when (and (>= grid-x 0) (< grid-x *grid-width*)
(>= grid-y 0) (< grid-y *grid-height*))
(case (sdl2:mouse-button-button event)
(:left (setf (aref *grid* grid-x grid-y)
(not (aref *grid* grid-x grid-y))))
(:right (save-pattern *pattern-file*))))))))

;; 메인 이벤트 루프 수정
(defun run-life ()
(sdl2:with-init (:video)
(sdl2:with-window (win :title "Game of Life" :w *width* :h *height*)
(sdl2:with-renderer (renderer win)
(initialize-grid t)
(sdl2:with-event-loop (:method :poll)
(:quit () t)
(:keydown (:keysym keysym)
(cond
((sdl2:scancode= (sdl2:scancode-value keysym) :scancode-space)
(setf *paused* (not *paused*)))
((sdl2:scancode= (sdl2:scancode-value keysym) :scancode-r)
(initialize-grid t))
((sdl2:scancode= (sdl2:scancode-value keysym) :scancode-l)
(load-pattern *pattern-file*))
((sdl2:scancode= (sdl2:scancode-value keysym) :scancode-escape)
(sdl2:push-event :quit))))

;; 마우스 이벤트 처리 추가
(:mousebuttondown (event)
(handle-mouse-event event))
(:mousebuttonup (event)
(handle-mouse-event event))

(:idle ()
(unless *paused*
(next-generation))
(render-grid renderer)
(sdl2:delay 50)))))))

(run-life)