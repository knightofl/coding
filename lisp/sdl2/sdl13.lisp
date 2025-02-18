(load "~/quicklisp/setup.lisp")
(ql:quickload "sdl2")

(defparameter *width* 800)
(defparameter *height* 600)
(defparameter *max-iterations* 100)

(defun mandelbrot (cx cy)
  (let ((zx 0.0)
        (zy 0.0)
        (i 0))
    (loop while (and (< (+ (* zx zx) (* zy zy)) 4.0)
                     (< i *max-iterations*))
          do (let ((temp (+ (- (* zx zx) (* zy zy)) cx)))
               (setf zy (+ (* 2.0 zx zy) cy))
               (setf zx temp)
               (incf i)))
    i))

(defun map-to-range (value from-min from-max to-min to-max)
  (+ to-min (* (/ (- value from-min) (- from-max from-min)) (- to-max to-min))))

(defun get-color (iter)
  (let ((t-value (/ iter *max-iterations*)))  ; `T` 대신 `t-value` 사용
    (values
     (min 255 (max 0 (floor (* 9 (* (1- t-value) t-value t-value t-value) 255))))  ; Red
     (min 255 (max 0 (floor (* 15 (* (1- t-value) t-value t-value) 255))))         ; Green
     (min 255 (max 0 (floor (* 8.5 (* (1- t-value) (1- t-value) t-value t-value) 255)))))))  ; Blue

(defun draw-mandelbrot (renderer)
  (sdl2:set-render-draw-color renderer 0 0 0 255)
  (sdl2:render-clear renderer)
  (dotimes (y *height*)
    (dotimes (x *width*)
      (let* ((cx (map-to-range x 0 *width* -2.5 1.0))
             (cy (map-to-range y 0 *height* -1.0 1.0))
             (iter (mandelbrot cx cy)))
        (if (= iter *max-iterations*)
            (sdl2:set-render-draw-color renderer 0 0 0 255)  ; Mandelbrot 집합 내부는 검은색
            (multiple-value-bind (r g b) (get-color iter)
              (sdl2:set-render-draw-color renderer r g b 255)))
        (sdl2:render-draw-point renderer x y))))
  (sdl2:render-present renderer))

(defun main ()
  (sdl2:with-init (:video)
    (sdl2:with-window (win :title "Mandelbrot Fractal (Color)" :w *width* :h *height* :flags '(:shown))
      (sdl2:with-renderer (renderer win :index -1 :flags '(:accelerated))
        (draw-mandelbrot renderer)  ; `renderer`를 `draw-mandelbrot` 함수에 전달
        (sdl2:with-event-loop (:method :poll)
          (:quit () t)
          (:keydown (:keysym keysym)
                    (when (sdl2:scancode= (sdl2:scancode-value keysym) :scancode-escape)
                      (sdl2:push-quit-event)))))))
   (sb-ext:gc :full t))

(main)