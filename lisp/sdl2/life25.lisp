(load "~/quicklisp/setup.lisp")
(ql:quickload "sdl2")

(defpackage :game-of-life
  (:use :common-lisp :sdl2))

(in-package :game-of-life)

;; 창 크기와 격자 설정
(defparameter *cell-size* 5)  ; 셀 한칸의 크기, 픽셀 단위.
(defparameter *rows* 100)       ; 화면에 표시되는 행수
(defparameter *cols* 100)       ; 화면에 표시되는 열수
(defparameter *window-width* (* *cols* *cell-size*))  ;; 창의 너비
(defparameter *window-height* (* *rows* *cell-size*)) ;; 창의 높이
(defparameter *buffer-padding* 2) ; 주변으로 추가할 줄 수 (2줄)
(defparameter *buffer-rows* (+ *rows* (* 2 *buffer-padding*))) ; 표시 영역 + 2줄 * 2 (위아래)
(defparameter *buffer-cols* (+ *cols* (* 2 *buffer-padding*))) ; 표시 영역 + 2줄 * 2 (좌우)
(defparameter *grid* (make-array (list *buffer-cols* *buffer-rows*) :initial-element nil)) ; 더 넓은 계산 영역
(defparameter *running* nil)
(defparameter *paused* t)  ; 초기 상태는 일시 정지
(defparameter *random* 0.1)
(defparameter *delay* 50)

;; 격자 초기화
(defun initialize-grid ()
  (loop for x from 0 below *buffer-cols* do
    (loop for y from 0 below *buffer-rows* do
      (setf (aref *grid* x y) nil))))

;; 랜덤 격자 생성
(defun randomize-grid ()
  (loop for x from 0 below *buffer-cols* do
    (loop for y from 0 below *buffer-rows* do
      (setf (aref *grid* x y) (if (< (random 1.0) *random*) t nil)))))

;; 이웃 셀의 수 계산
(defun count-neighbors (x y)
  (let ((count 0))
    (loop for dx from -1 to 1 do
      (loop for dy from -1 to 1 do
        (unless (and (= dx 0) (= dy 0))
          (let ((nx (+ x dx))
                (ny (+ y dy)))
            ;; 경계를 넘어가는 셀은 무시
            (when (and (>= nx 0) (< nx *buffer-cols*)
                       (>= ny 0) (< ny *buffer-rows*)
                       (aref *grid* nx ny))
              (incf count))))))
    count))

;; 다음 상태 계산
(defun next-generation ()
  (let ((new-grid (make-array (list *buffer-cols* *buffer-rows*) :initial-element nil)))
    (loop for x from 0 below *buffer-cols* do
      (loop for y from 0 below *buffer-rows* do
        (let ((neighbors (count-neighbors x y)))
          (setf (aref new-grid x y)
                (if (aref *grid* x y)
                    (or (= neighbors 2) (= neighbors 3))
                    (= neighbors 3))))))
    (setf *grid* new-grid)))

;; 렌더링
(defun render-grid (renderer)
  (sdl2:set-render-draw-color renderer 0 0 0 255) ; 배경 검정색
  (sdl2:render-clear renderer)
  (sdl2:set-render-draw-color renderer 0 255 0 255) ; 셀 녹색
  ;; 화면에 표시되는 영역만 렌더링
  (loop for x from *buffer-padding* below (+ *cols* *buffer-padding*) do
    (loop for y from *buffer-padding* below (+ *rows* *buffer-padding*) do
      (when (aref *grid* x y)
        (sdl2:render-fill-rect renderer
                               (sdl2:make-rect (* (- x *buffer-padding*) *cell-size*)
                                               (* (- y *buffer-padding*) *cell-size*)
                                               *cell-size*
                                               *cell-size*)))))
  (sdl2:render-present renderer))

;; 마우스 클릭으로 셀 상태 토글
(defun toggle-cell (x y)
  (let ((grid-x (+ *buffer-padding* (floor x *cell-size*))) ; 화면 좌표를 버퍼 좌표로 변환
        (grid-y (+ *buffer-padding* (floor y *cell-size*))))
    (when (and (< grid-x *buffer-cols*) (< grid-y *buffer-rows*))
      (setf (aref *grid* grid-x grid-y) (not (aref *grid* grid-x grid-y))))))

;; 격자 상태를 파일로 저장
(defun save-grid-to-file (filename)
  (with-open-file (stream filename :direction :output :if-exists :supersede)
    (loop for y from 0 below *buffer-rows* do
      (loop for x from 0 below *buffer-cols* do
        (write-char (if (aref *grid* x y) #\1 #\0) stream))
      (write-char #\newline stream))))

;; 파일에서 격자 상태 읽기
(defun load-grid-from-file (filename)
  (with-open-file (stream filename :direction :input)
    (loop for y from 0 below *buffer-rows* do
      (loop for x from 0 below *buffer-cols* do
        (let ((char (read-char stream)))
          (setf (aref *grid* x y) (if (char= char #\1) t nil))))
      (read-char stream)))) ; 줄바꿈 문자 소비

;; 메인 루프
(defun run-life ()
  (sdl2:with-init (:video)
    (sdl2:with-window (win :title "Conway's Game of Life" :w *window-width* :h *window-height*)
      (sdl2:with-renderer (renderer win)
        (initialize-grid)
        (sdl2:with-event-loop (:method :poll)
          (:quit () t)
          (:keydown (:keysym keysym) ; keysym 변수 사용
            (let ((scancode (sdl2:scancode-value keysym))) ; 스캔 코드 추출
              (format t "Key pressed: ~a~%" scancode) ; 눌린 키의 스캔 코드 출력
              (case scancode
                (44         (setf *paused* (not *paused*)))         ; 스페이스바로 일시 정지/재개
                (6          (initialize-grid))                      ; C 키로 격자 재설정
                (21         (randomize-grid))                       ; R 키로 랜덤격자 생성
                (82         (incf *delay* 10))                      ; ↑ 키로 딜레이 증가 
                (81         (when (> *delay* 10) (decf *delay* 10))); ↓ 키로 딜레이 감소  
                (22         (save-grid-to-file "grid.txt")          ; S 키로 격자 저장
                            (format t "Grid saved to grid.txt~%"))
                (15         (load-grid-from-file "grid.txt")        ; L 키로 격자 불러오기
                            (format t "Grid loaded from grid.txt~%"))
                (41         (sdl2:push-event :quit))                ; ESC 키로 종료
                (otherwise  (format t "Unknown key pressed~%")))))  ; 알 수 없는 키 입력
          (:mousebuttondown (:button button :x x :y y)
            (when (= button 1) ; 왼쪽 마우스 버튼
              (toggle-cell x y)))
          (:idle ()
            (unless *paused* (next-generation))
            (render-grid renderer)
            (sdl2:delay *delay*))))))
  (sb-ext:gc :full t))

;; 게임 실행
(run-life)