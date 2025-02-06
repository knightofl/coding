(load "~/quicklisp/setup.lisp")
(ql:quickload "sdl2")

(defun show-window ()
  "640x480 크기의 파란색 배경 창을 띄우고, 엔터 입력 시 종료."
  (sdl2:with-init (:video)
    (sdl2:with-window (win 
                       :title "SDL2 Window" 
                       :x 100 :y 100         ; 창의 위치 (선택사항)
                       :w 640 :h 480         ; 너비와 높이
                       :flags nil)           ; 추가 옵션 없으면 nil로 설정
      (sdl2:with-renderer (renderer win)
        ;; 파란색 배경 (RGBA: 0, 0, 255, 255)로 창 클리어
        (sdl2:set-render-draw-color renderer 0 0 255 255)
        (sdl2:render-clear renderer)
        (sdl2:render-present renderer)

        (sdl2:with-event-loop (:method :poll)
          (:quit () t)
          (:idle ()
                 (sdl2:render-clear renderer)
                 (sdl2:render-present renderer))))))
  (sb-ext:gc :full t))

(show-window)