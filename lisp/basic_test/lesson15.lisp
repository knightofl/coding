(defclass apprentice-wizard (wizard) ())

(let ((junior (make-instance 'apprentice-wizard))
      (old-stick (make-instance 'magic-stick)))
     (make-attack junior old-stick))

(defmethod make-attack ((avatar apprentice-wizard) (weapon magic-stick))
    (format t "I am just learning~%"))

(defmethod print-object ((obj arrrentice-wizard) stream)
    (format stream "I am an apprentice~%"))

(print (make-instance 'apprentice-wizard))
