(load "~/quicklisp/setup.lisp")
(ql:quickload "sdl2")

(defpackage :sierpinski-triangle
  (:use :common-lisp :sdl2))

(in-package :sierpinski-triangle)

(defparameter *window-width* 640)
(defparameter *window-height* 480)

(defun midpoint (x1 y1 x2 y2)
  "두 점 (x1, y1)과 (x2, y2)의 중점을 정수로 변환하여 반환한다."
  (values (truncate (+ x1 x2) 2) (truncate (+ y1 y2) 2)))

(defun draw-sierpinski (renderer x1 y1 x2 y2 x3 y3 depth)
  "재귀적으로 시에르핀스키 삼각형을 그린다."
  (when (> depth 0)
    (multiple-value-bind (mx1 my1) (midpoint x1 y1 x2 y2)
      (multiple-value-bind (mx2 my2) (midpoint x2 y2 x3 y3)
        (multiple-value-bind (mx3 my3) (midpoint x3 y3 x1 y1)
          ;; 삼각형을 그린다.
          (sdl2:render-draw-line renderer mx1 my1 mx2 my2)
          (sdl2:render-draw-line renderer mx2 my2 mx3 my3)
          (sdl2:render-draw-line renderer mx3 my3 mx1 my1)

          ;; 재귀적으로 삼각형을 분할하여 그린다.
          (draw-sierpinski renderer x1 y1 mx1 my1 mx3 my3 (- depth 1))
          (draw-sierpinski renderer mx1 my1 x2 y2 mx2 my2 (- depth 1))
          (draw-sierpinski renderer mx3 my3 mx2 my2 x3 y3 (- depth 1)))))))

(defun show-window ()
  "시에르핀스키 삼각형을 그리는 SDL2 창을 띄운다."
  (sdl2:with-init (:video)
    (sdl2:with-window (win :title "Sierpinski Triangle" :w *window-width* :h *window-height*)
      (sdl2:with-renderer (renderer win)
        ;; 배경을 검은색으로 설정
        (sdl2:set-render-draw-color renderer 0 0 0 255)
        (sdl2:render-clear renderer)

        ;; 삼각형 색상을 흰색으로 설정
        (sdl2:set-render-draw-color renderer 255 255 255 255)

        ;; 초기 삼각형 좌표 설정
        (let ((x1 (/ *window-width* 2))
              (y1 50)
              (x2 50)
              (y2 (- *window-height* 50))
              (x3 (- *window-width* 50))
              (y3 (- *window-height* 50)))
          (draw-sierpinski renderer x1 y1 x2 y2 x3 y3 5))

        ;; 화면에 그리기
        (sdl2:render-present renderer)

        ;; 이벤트 루프 (X 버튼 클릭하면 종료)
        (loop
          (sdl2:with-event-loop
            (:quit () (return))))))))  ;; ✅ 올바르게 수정됨

(show-window)
