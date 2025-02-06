(load "~/quicklisp/setup.lisp")
(ql:quickload "sdl2")

(defpackage :basic-sdl2-window
  (:use :common-lisp :sdl2))

(in-package :basic-sdl2-window)

(defparameter *window-width* 640)
(defparameter *window-height* 480)

(defun create-window ()
  (sdl2:with-init (:video)
    (sdl2:with-window (win :title "SDL2 Window" :w *window-width* :h *window-height*)
      (sdl2:with-renderer (renderer win)
        (loop
          (let ((event (sdl2:wait-event)))
            (cond
              ((and event (sdl2:event-type event) (eq (sdl2:event-type event) :quit))
               (return))  ;; ESC로 종료
              ((and event (sdl2:event-type event) (eq (sdl2:event-type event) :keydown))
               (let ((keysym (sdl2:event-keysym event)))
                 (when (eq (sdl2:scancode-value keysym) :scancode-escape)
                   (return))))))  ;; ESC 키로 종료
          (sdl2:render-clear renderer)
          (sdl2:set-render-draw-color renderer 0 0 255 255)  ;; 배경색 파랑
          (sdl2:render-present renderer)
          (sdl2:delay 16))))))

(create-window)