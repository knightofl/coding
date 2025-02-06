(defun save-pattern (filename grid)
  (with-open-file (out filename :direction :output :if-exists :supersede)
    (dolist (row grid)
      (dolist (cell row)
        (write-char (if cell #\# #\.) out))
    (terpri out))))

(defun load-pattern (filename)
  (if (probe-file filename)
      (with-open-file (in filename :direction :input)
        (loop for line = (read-line in nil)
              while line
              collecting (map 'vector (lambda (ch) (if (char= ch #\#) 1 0) line)) into grid
              finally (return (coerce grid 'vector))))
        (error "File not found: ~A" filename)))

(defun start-new-game (fliename)
  (setf *grid* (load-pattern filename))
  (run-life))