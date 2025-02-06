(load "~/quicklisp/setup.lisp")
(ql:quickload "sdl2")

;;; Configuration
(defparameter *width*  800)
(defparameter *height* 600)
(defparameter *max-depth* 7)
(defparameter *background-color* '(0 0 0 255))
(defparameter *triangle-color*   '(0 255 0 255))

;;; Math Utilities
(defun mid (a b) (floor (+ a b) 2))

;;; Drawing Core
(defun draw-triangle (renderer p1 p2 p3 depth)
  (destructuring-bind ((x1 y1) (x2 y2) (x3 y3)) (list p1 p2 p3)
    (if (zerop depth)
        ;; Base case: Draw the triangle
        (progn
          (sdl2:render-draw-line renderer x1 y1 x2 y2)
          (sdl2:render-draw-line renderer x2 y2 x3 y3)
          (sdl2:render-draw-line renderer x3 y3 x1 y1))
        ;; Recursive case: Split and recurse
        (let ((m12 (list (mid x1 x2) (mid y1 y2)))
              (m23 (list (mid x2 x3) (mid y2 y3)))
              (m31 (list (mid x3 x1) (mid y3 y1))))
          (draw-triangle renderer p1 m12 m31 (1- depth))
          (draw-triangle renderer m12 p2 m23 (1- depth))
          (draw-triangle renderer m31 m23 p3 (1- depth))))))

;;; Main Drawing Function
(defun draw-sierpinski (renderer)
  (destructuring-bind (r g b a) *background-color*
    (sdl2:set-render-draw-color renderer r g b a)
    (sdl2:render-clear renderer))
  
  (destructuring-bind (r g b a) *triangle-color*
    (sdl2:set-render-draw-color renderer r g b a)
    (let ((p1 (list (mid *width* 0) 50))          ; Top
          (p2 (list 50 (- *height* 50)))          ; Left
          (p3 (list (- *width* 50) (- *height* 50)))) ; Right
      (draw-triangle renderer p1 p2 p3 *max-depth*)))
  
  (sdl2:render-present renderer))

;;; Window Management
(defun run-sierpinski ()
  (sdl2:with-init (:video)
    (sdl2:with-window (win :title "Sierpiński Masterpiece" :w *width* :h *height* :flags '(:shown))
      (sdl2:with-renderer (renderer win)
        (draw-sierpinski renderer)
        (sdl2:with-event-loop (:method :poll)
          (:quit () t)
          (:keydown (:keysym keysym)
                    (when (sdl2:scancode= (sdl2:scancode-value keysym) :scancode-escape)
                      (sdl2:push-quit-event)))))))
  (sb-ext:gc :full t))

;;; Start the show!
(run-sierpinski)