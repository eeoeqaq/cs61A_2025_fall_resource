(define-macro (assign sym1 sym2 expr1 expr2)
  `(begin
     (define ,sym1 ,expr1)
     (define ,sym2 ,(eval expr2))))

(assign x y (+ 1 1) 3)
(assign x y y x)
(expect x 3)
(expect y 2)

(define-macro (switch expr cases)
  `(begin
	(define val ,expr)
	,(cons 'cond
	(map (lambda (case) (cons
			`(equal? val ,(car case))
			(cdr case)))
		cases))))
