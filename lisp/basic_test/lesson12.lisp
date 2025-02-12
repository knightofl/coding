(defclass circle ()
    ((radius :initarg :radius :initform 0 :accessor radius)))

(defclass rectangle ()
    ((base   :initarg :base   :initform 0 :accessor base)
     (height :initarg :height :initform 0 :accessor height)))

(defclass colored-object ()
    ((color :initarg :color
            :initform (error "You have to provide the initial color.")
            :accessor color)))

(defclass colored-circle (circle colored-object)
    ())

(defclass colored-rectangle (rectangle colored-object)
    ())