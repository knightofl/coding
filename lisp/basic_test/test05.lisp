;; true, false

(eq nil 'nil)
(eq '() ())
(eq nil ())

(if '()
    'i-am-true
    'i-am-false)

(defun my-length (list)
           (if list
               (1+ (my-length (cdr list)))
               0))
(my-length '(a b c d))

(if (= (+ 1 2) 3)
    'yes
    'no)

(if (oddp 3)
    'odd
    'even)

(if (evenp 4)
    'even
    'odd)

(defvar *number-odd* nil)
(if (oddp 3)
    (progn (setf *number-odd* t)
               'odd-number)
    'even-number)

(defvar *number-odd* nil)
(when (oddp 3)
    (setf *number-odd* t)
    'odd-number)
(unless (evenp 3)
    (setf *number-odd* nil)
    'even-number)

(defun pudding-eater (person)                                          
    (cond ((eq person 'henry) (setf *arch-enemy* 'stupid-lisp-alien)
          '(curse you lisp alien? you ate my pudding))                  
    ((eq person 'johnny) (setf *arch-enemy* 'useless-old-johnny)   
          '(i hope you choked on my pudding johnny))                    
    (t    '(why you eat my pudding stranger?))))

(defun pudding-eater (person)                                          
    (case person
        ((henry)   (setf *arch-enemy* 'stupid-lisp-alien)
                   '(curse you lisp alien? you ate my pudding))                  
        ((johnny)  (setf *arch-enemy* 'useless-old-johnny)   
                   '(i hope you choked on my pudding johnny))                    
        (otherwise '(why you eat my pudding stranger?))))

(and (oddp 3) (evenp 2))
(or (oddp 2) (evenp 2))

(defparameter *is-it-even* nil)
(or (oddp 4) (setf *is-it-even* t)

(member 3 '(1 2 3 4 5))

(find-if #'evenp '(1 2 3 4 5))
(find-if #'oddp '(1 2 3 4 5))
(find-if #'null '(1 2 nil 3))

(defparameter *fruit* 'apple)
(cond ((eq *fruit* 'apple) 'its-an-apple)
      ((eq *fruit* 'orange) 'its-an-orange))

(equal 'apple 'apple)
(equal (list 1 2 3) (list 1 2 3))
(equal '(1 2 3) (cons 1 (cons 2 (cons 3 ()))))
(equal 5 5)
(equal 2.5 2.5)
(equal "foo" "foo")
(equal #\a #\a)

(eql 'foo 'foo)
(eql 3.14 3.14)
(eql #\a #\a)

(equalp "Bob Smith" "bob smith")
(equalp 1 1.0)