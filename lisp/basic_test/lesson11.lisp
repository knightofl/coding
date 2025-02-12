(defclass circle ()
    ((radius :initarg :radius :initform 0 :accessor radius)))

(defclass rectangle ()
    ((base   :initarg :base   :initform 0 :accessor base)
     (height :initarg :height :initform 0 :accessor height)))
    

(defparameter *my-circle* (make-instance 'circle :radius 10))
(princ (radius *my-circle*))
(setf (radius *my-circle*) 20)

(defparameter *my-rect* (make-instance 'rectangle :base 10 :height 12))
(princ (height *my-rect*))

(defclass colored-circle (circle)
    ((color :initarg :color :accessor color)))

(defparameter *green-circle*
    (make-instance 'colored-circle :radius 20 :color :green))

(print (slot-value *green-circle* 'radius))

(defclass colored-rectangle (rectangle)
    ((color :initarg :color
            :initform (error "You have to provide the initial color.")
            :accessor color)))