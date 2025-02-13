(defclass avatar      ()        ())
(defclass warrior     (avatar)  ())
(defclass wizard      (avatar)  ())

(defclass weapon      ()        ())
(defclass sword       (weapon)  ())
(defclass magic-stick (weapon)  ())

(defgeneric make-attack (avatar weapon))

(defmethod make-attack ((avatar warrior) (weapon sword))
    (format t "Great physical attack~%"))

(defmethod make-attack ((avatar wizard) (weapon sword))
    (format t "Bad physical attack~%"))

(let ((war (make-instance 'warrior))
      (wiz (make-instance 'wizard))
      (big-sword (make-instance 'sword))
      (old-stick (make-instance 'magic-stick)))
     (make-attack war big-sword)
     (make-attack war old-stick)
     (make-attack wiz big-sword)
     (make-attack wix old-stick))

 