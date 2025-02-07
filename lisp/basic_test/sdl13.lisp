(load "~/quicklisp/setup.lisp")
(ql:quickload "sdl2")

;;; 화면 크기 및 설정
(defparameter *width*  800)
(defparameter *height* 600)
(defparameter *max-iteration* 300)  ;; 반복 횟수 증가로 디테일 개선
(defparameter *background-color* '(0 0 0 255))

;;; 컬러 변환 함수 (스무딩 적용)
;;; 컬러 변환 함수 (스무딩 적용)
(defun get-color (iteration)
  (if (= iteration *max-iteration*)
      '(0 0 0 255)  ;; 내부는 검은색
      (let* ((smooth (float (/ iteration *max-iteration*)))  ;; 정규화
             (r (round (* 255 (sqrt smooth))))
             (g (round (* 255 (* smooth smooth))))
             (b (round (* 255 (sin (* smooth 3.1415))))))
        (list r g b 255))))  ;; RGBA 색상 반환

;;; 만델브로 계산
(defun mandelbrot (renderer)
  (loop for px from 0 below *width* do
    (loop for py from 0 below *height* do
      (let* ((x0 (+ -2.0 (* 3.0 (/ px *width*))))  ;; x 범위: -2.0 ~ 1.0
             (y0 (+ -1.5 (* 3.0 (/ py *height*)))) ;; y 범위: -1.5 ~ 1.5
             (x 0.0) (y 0.0) (iteration 0))
        (loop while (and (< (+ (* x x) (* y y)) 4) (< iteration *max-iteration*)) do
          (psetf x (+ (* x x) (- (* y y)) x0)
                 y (+ (* 2 x y) y0)
                 iteration (1+ iteration)))
        (destructuring-bind (r g b a) (get-color iteration)
          (sdl2:set-render-draw-color renderer r g b a)
          (sdl2:render-draw-point renderer px py))))))

;;; 창 열고 렌더링
(defun run-mandelbrot ()
  (sdl2:with-init (:video)
    (sdl2:with-window (win :title "Mandelbrot Set" :w *width* :h *height*)
      (sdl2:with-renderer (renderer win)
        (mandelbrot renderer)
        (sdl2:render-present renderer)  ;; 화면 업데이트
        (sdl2:with-event-loop (:method :poll)
          (:quit () t)
          (:keydown (:keysym keysym)
                    (when (sdl2:scancode= (sdl2:scancode-value keysym) :scancode-escape)
                      (sdl2:push-quit-event)))))))
  (sb-ext:gc :full t))

;;; 실행
(run-mandelbrot)
