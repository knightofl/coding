(load "~/quicklisp/setup.lisp")
(ql:quickload "sdl2")

(defparameter *width* 800)
(defparameter *height* 600)
(defparameter *max-depth* 7)  ; 재귀 깊이

(defun draw-triangle (renderer x1 y1 x2 y2 x3 y3 depth)
  (if (<= depth 0)
      (progn
        (sdl2:render-draw-line renderer x1 y1 x2 y2)
        (sdl2:render-draw-line renderer x2 y2 x3 y3)
        (sdl2:render-draw-line renderer x3 y3 x1 y1))
      (let* ((x12 (/ (+ x1 x2) 2))
             (y12 (/ (+ y1 y2) 2))
             (x23 (/ (+ x2 x3) 2))
             (y23 (/ (+ y2 y3) 2))
             (x31 (/ (+ x3 x1) 2))
             (y31 (/ (+ y3 y1) 2)))
        (draw-triangle renderer x1 y1 x12 y12 x31 y31 (1- depth))
        (draw-triangle renderer x12 y12 x2 y2 x23 y23 (1- depth))
        (draw-triangle renderer x31 y31 x23 y23 x3 y3 (1- depth)))))

(defun draw-sierpinski (renderer)
  (sdl2:set-render-draw-color renderer 255 255 255 255)  ; 배경색: 흰색
  (sdl2:render-clear renderer)
  (sdl2:set-render-draw-color renderer 0 0 0 255)  ; 삼각형 색상: 검은색
  (let ((x1 (/ *width* 2))
        (y1 50)
        (x2 50)
        (y2 (- *height* 50))
        (x3 (- *width* 50))
        (y3 (- *height* 50)))
    (draw-triangle renderer x1 y1 x2 y2 x3 y3 *max-depth*))
  (sdl2:render-present renderer))

(defun main ()
  (sdl2:with-init (:video)
    (sdl2:with-window (win :title "Sierpiński Triangle" :w *width* :h *height* :flags '(:shown))
      (sdl2:with-renderer (renderer win :index -1 :flags '(:accelerated))
        (draw-sierpinski renderer)
        (sdl2:with-event-loop (:method :poll)
          (:quit () t)
          (:keydown (:keysym keysym)
                    (when (sdl2:scancode= (sdl2:scancode-value keysym) :scancode-escape)
                      (sdl2:push-quit-event))))))))

(main)