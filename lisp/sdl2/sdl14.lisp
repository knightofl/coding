(load "~/quicklisp/setup.lisp")
(ql:quickload "sdl2")

;;; Configuration
(defparameter *width*  800)
(defparameter *height* 600)
(defparameter *max-iteration* 500)
(defparameter *background-color* '(0 0 0 255))

;;; Convert HSV to RGB
(defun hsv-to-rgb (h s v)
  (let* ((c (* v s))
         (x (* c (- 1 (abs (- (/ h 60) (floor (/ h 120)) 2)))))
         (m (- v c))
         (rgb (cond ((< h 60)  (list c x 0))
                    ((< h 120) (list x c 0))
                    ((< h 180) (list 0 c x))
                    ((< h 240) (list 0 x c))
                    ((< h 300) (list x 0 c))
                    (t        (list c 0 x)))) )
    (mapcar (lambda (n) (floor (* (+ n m) 255))) rgb)))

;;; Get Color based on iteration count
(defun get-color (iteration)
  (if (= iteration *max-iteration*)
      '(0 0 0) ; Black for points inside the set
      (let* ((smooth-iter (+ iteration 1 (- (/ (log (log (+ 1 iteration))) (log 2)))))
             (hue (mod (* 360 (/ smooth-iter *max-iteration*)) 360))
             (rgb (hsv-to-rgb hue 1 1)))
        rgb)))

;;; Mandelbrot Computation
(defun mandelbrot (x y)
  (let* ((zx 0.0) (zy 0.0) (cx x) (cy y) (iteration 0))
    (loop while (and (< (+ (* zx zx) (* zy zy)) 4) (< iteration *max-iteration*))
          do (let ((temp (- (* zx zx) (* zy zy) cx)))
               (setf zy (+ (* 2 zx zy) cy))
               (setf zx temp)
               (incf iteration)))
    iteration))

;;; Draw Mandelbrot Set
(defun draw-mandelbrot (renderer)
  (loop for px from 0 below *width* do
    (loop for py from 0 below *height* do
      (let* ((x (/ (- (* 3.5 px) (* 2.5 *width*)) *width*))
             (y (/ (- (* 2.0 py) (* *height*)) *height*))
             (iteration (mandelbrot x y))
             (color (get-color iteration)))
        (destructuring-bind (r g b) color
          (sdl2:set-render-draw-color renderer r g b 255)
          (sdl2:render-draw-point renderer px py)))))
  (sdl2:render-present renderer))

;;; Window Management
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

;;; Start rendering
(run-mandelbrot)
