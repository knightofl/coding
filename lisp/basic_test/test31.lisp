(defparammeter *my-circle*
    (make-instance 'circle :radius 10))
(princ (area *my-circle*))

(defparameter *my-rect* 
    (make-instance 'rectangle :base 10 :height 12))
(princ (area *my-rect*))
