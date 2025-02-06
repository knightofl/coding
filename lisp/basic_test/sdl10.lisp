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
        ;; 콘솔 입력으로 종료 대기
        (format t "창이 열렸습니다. 종료하려면 엔터 키를 누르세요.~%")
        (read-line)))))

(show-window)