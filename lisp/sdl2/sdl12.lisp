(load "~/quicklisp/setup.lisp")
(ql:quickload "sdl2")

;;; Configuration
(defparameter *width* 800)
(defparameter *height* 600)
(defparameter *max-iterations* 100)
(defparameter *zoom* 1.0)
(defparameter *center-x* -0.5)
(defparameter *center-y* 0.0)

(defun mandelbrot (cr ci)
  "Compute the Mandelbrot set escape time."
  (loop with zr = 0.0d0 and zi = 0.0d0
        for i from 0 below *max-iterations*
        when (> (+ (* zr zr) (* zi zi)) 4.0d0) return i
        do (psetq zr (+ (* zr zr) (- (* zi zi)) cr)
                  zi (+ (* 2 zr zi) ci))
        finally (return *max-iterations*)))

(defun scale (value min1 max1 min2 max2)
  "값을 [min1, max1] 범위에서 [min2, max2] 범위로 변환"
  (+ min2 (* (- value min1) (/ (- max2 min2) (- max1 min1)))))

(defun draw-mandelbrot (renderer)
  (dotimes (px *width*)
    (dotimes (py *height*)
      (let* ((x0 (scale px 0 *width* -2.0 1.0))
             (y0 (scale py 0 *height* -1.5 1.5))
             (x 0.0)
             (y 0.0)
             (iteration 0)
             (max-iteration 255))  ;; 여기서 선언
        (loop while (< (+ (* x x) (* y y)) 4.0)
              while (< iteration max-iteration) do
          (let ((xtemp (- (* x x) (* y y) x0)))
            (setf y (+ (* 2 x y) y0))
            (setf x xtemp)
            (incf iteration)))
        (let ((color (floor (* 255 (/ iteration max-iteration)))))
          (sdl2:set-render-draw-color renderer color color color 255)
          (sdl2:render-draw-point renderer px py)))))  ;; 여기 수정
  (sdl2:render-present renderer))  ;; 렌더링 갱신


(defun run-mandelbrot ()
  (sdl2:with-init (:video)
    (sdl2:with-window (win :title "Mandelbrot Fractal" :w *width* :h *height* :flags '(:shown))
      (sdl2:with-renderer (renderer win)
        (draw-mandelbrot renderer)
        (sdl2:with-event-loop (:method :poll)
          (:quit () t)
          (:keydown (:keysym keysym)
                    (when (sdl2:scancode= (sdl2:scancode-value keysym) :scancode-escape)
                      (sdl2:push-quit-event)))))))
  (sb-ext:gc :full t))

;;; Start rendering Mandelbrot set
(run-mandelbrot)