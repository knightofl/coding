;; 10x10 크기의 0으로 채워진 격자 생성
(defparameter *rows* 30)
(defparameter *cols* 40)

(defun make-grid ()
  (make-array (list *rows* *cols*) :element-type '(integer 0 1) :initial-element 0))

;; 30% 확률로 셀이 살아있는 격자 생성
(defun randomize-grid (grid)
  (loop for i below *rows*
        do (loop for j below *cols*
                 do (setf (aref grid i j) (if (< (random 1.0) 0.3) 1 0)))))

;; 각 셀의 8방향 이웃을 확인하는 함수
(defun count-neighbors (grid x y)
  (let ((count 0))
    (loop for dx in '(-1 -1 -1  0  0  1  1  1)
          for dy in '(-1  0  1 -1  1 -1  0  1)
          do (let ((nx (+ x dx))
                   (ny (+ y dy)))
                (when (and (>= nx 0) (< nx *rows*)
                           (>= ny 0) (< ny *cols*))
                    (incf count (aref grid nx ny)))))
    count))

;; 기존격자를 검사하고 새 격자를 만들어 반환
(defun next-generation (grid)
  (let ((new-grid (make-grid)))
    (loop for i below *rows*
          do (loop for j below *cols*
                   do (let ((alive (aref grid i j))
                            (neighbors (count-neighbors grid i j)))
                        (setf (aref new-grid i j)
                              (if (or (and (= alive 1) (or (= neighbors 2) (= neighbors 3)))
                                      (and (= alive 0) (= neighbors 3)))
                                  1
                                  0)))))
    new-grid))

;; 살아있는 셀은 'O', 죽은 셀은 '.'으로 출력
(defun print-grid (grid)
  (loop for i below *rows*
        do (loop for j below *cols*
                 do (format t "~A " (if (= (aref grid i j) 1) "O" ".")))
        (format t "~%")))

(defun clear-screen ()
  (format t "~c[2J~c[H" #\ESC #\ESC))

;; 0.5초마다 격자를 출력하고 다음 세대로 진행
(defun run-life (steps)
  (let ((grid (make-grid)))
    (randomize-grid grid)
    (loop for i below steps
          do (progn
                (clear-screen)
                (print-grid grid)
                (setf grid (next-generation grid))
                (sleep 0.5)))))

;; 게임 실행
(run-life 200)