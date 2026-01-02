(define (mymap1 procedure s)
    (if (null? s)
        nil
        (cons (procedure (car s)) (mymap1 procedure (cdr s)))))

(define (mymap2 pro s)
    (define (reverse-map s re)
        (if (null? s)
            re
            (reverse-map (cdr s) (cons (pro (car s)) re))))
    (reverse(reverse-map s nil)))

(define (reverse s)
    (define(mem s re)
        (if (null? s)
            re
            (mem (cdr s) (cons (car s) re))))
    (mem s nil))
;;tranform a non-tail-recur version scheme apply to a tail-recur version 
;;how will the interpreter apply it in python?
;;
