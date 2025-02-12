(defmethod area ((shape circle))
    (* pi (radius shape) (radius shape)))

(defmethod area ((shape rectangle))
    (* (base shape) (height shape)))

(defgeneric area (shape)
    (:documentation "Compute the area of a ahape."))

(princ (area *my-circle*))
(princ (area *my-rect*))