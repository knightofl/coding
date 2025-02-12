*package*
(type-of *package*)

:cl
(eql :cl keyword:cl)
(eql :cl ':cl)

(describe 'and)

*paackage*
(in-package :cl)

(defpackage :com.example
  (:use :cl))

(im-package :com.example)

(dfun test () "test from th example package")

(defpackage :com.example2
  (:use :cl)
  (:import-from :com.example :test)
  (:export :test2))

(in-package :com.example2)

(defun test2 () (test))