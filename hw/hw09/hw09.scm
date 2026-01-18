(define (curry-cook formals body) 
  (if (null? (cdr formals))
      (list 'lambda (list (car formals)) body)
      (list 'lambda 
            (list (car formals)) 
            (curry-cook (cdr formals) body))))

;;(curry-cook '(x y) '(+ x y))
;;(lambda (x) (lambda (y) (+ x y)))
;; We return a program as a list.

; ((f 1) 1)
; 2


(define (curry-consume curry args)
  (if (null? args)
      curry
      (curry-consume (curry (car args)) (cdr args))))

(define-macro (switch expr options)
  (switch-to-cond (list 'switch expr options)))

(define (switch-to-cond switch-expr)
  (cons 'cond
        (map (lambda (option)
               (cons  (list 'equal? 
                            (car (cdr switch-expr)) 
                            (car option)) 
                      (cdr option)))
             (car (cdr (cdr switch-expr))))))


