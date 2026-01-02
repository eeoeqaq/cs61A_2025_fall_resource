import sys

from link import *
from scheme_utils import *
from scheme_reader import read_line
from scheme_builtins import create_global_frame
from ucb import main, trace

##############
# Eval/Apply #
##############

#不确定传入参数数量时的妥协
def scheme_eval(expr, env, _=None): # Optional third argument is ignored
    """Evaluate Scheme expression EXPR in Frame ENV.
    take in a Link/pyint/pystr, return the value.
    >>> expr = read_line('(+ 2 2)')
    >>> expr
    Link('+', Link(2, Link(2)))
    >>> scheme_eval(expr, create_global_frame())
    4
    """
    # Evaluate atoms
    if scheme_symbolp(expr):
        return env.lookup(expr)
    elif self_evaluating(expr):
        return expr

    # All non-atomic expressions are lists (combinations)
    if not scheme_listp(expr):
        raise SchemeError('malformed list: {0}'.format(repl_str(expr)))
    first, rest = expr.first, expr.rest

    from scheme_forms import SPECIAL_FORMS # Import here to avoid a cycle when modules are loaded
    #和schemeapply重复？
    if scheme_symbolp(first) and first in SPECIAL_FORMS:
        return SPECIAL_FORMS[first](rest, env)
    else:
        # BEGIN PROBLEM 3
        #quotation,first need to be evaluated
        if not isinstance(first,Procedure):
            first = scheme_eval(first,env)
        #nil进入self_evaluating
        rest=map_link((lambda x:scheme_eval(x,env)),rest)
        return scheme_apply(first,rest,env)
        # END PROBLEM 3
'''
>>>(1)
>>>SchemeError("1 is not callable")   
'''
def scheme_apply(procedure, args, env):
    """Apply Scheme PROCEDURE to argument values ARGS (a Scheme list(instance of List class)) in
    Frame ENV, the current environment."""
    validate_procedure(procedure)
    #frame类的实例 的 parent属性 模拟作用域的层层递进
    if not isinstance(env, Frame):
       assert False, "Not a Frame: {}".format(env)
    if isinstance(procedure, BuiltinProcedure):
        # BEGIN PROBLEM 2
        pyargs=[]
        while args is not nil:
            #有（pair？）这样的函数
            pyargs.append(args.first)
            args=args.rest
        func=procedure.py_func
        if procedure.need_env:
            pyargs.append(env)
        # END PROBLEM 2
        try:
            # BEGIN PROBLEM 2
            return func(*pyargs)
            # END PROBLEM 2
        except TypeError as err:
            raise SchemeError('incorrect number of arguments: {0}'.format(procedure))
    elif isinstance(procedure, LambdaProcedure):
        # BEGIN PROBLEM 9
        new_env=procedure.env.make_child_frame(procedure.formals,args)
        expressions=procedure.body
        while expressions.rest is not nil:
            scheme_eval(expressions.first,new_env)
            expressions=expressions.rest
        return scheme_eval(expressions.first,new_env,True)
        # END PROBLEM 9
    elif isinstance(procedure, MuProcedure):
        # BEGIN PROBLEM 11
        new_env=env.make_child_frame(procedure.formals,args)
        expressions=procedure.body
        while expressions.rest is not nil:
            scheme_eval(expressions.first,new_env)
            expressions=expressions.rest
        return scheme_eval(expressions.first,new_env,True)
        # END PROBLEM 11
    else:
        assert False, "Unexpected procedure: {}".format(procedure)

def eval_all(expressions, env, state=False):
    """Evaluate each expression in the Scheme list EXPRESSIONS in
    Frame ENV (the current environment) and return the value of the last.

    >>> eval_all(read_line("(1)"), Frame(None))
    1
    >>> eval_all(read_line("(1 2)"), Frame(None))
    2
    """
    # BEGIN PROBLEM 6
    if expressions is nil:
        return None
    while expressions!=nil:
        a=scheme_eval(expressions.first, env, state)
        expressions=expressions.rest 
    return a # replace this with lines of your own code
    # END PROBLEM 6

###################################
# Extra Challenge: Tail Recursion #
###################################

class Unevaluated:
    """An expression and an environment in which it is to be evaluated."""

    def __init__(self, expr, env):
        """Expression EXPR to be evaluated in Frame ENV."""
        self.expr = expr
        self.env = env

def complete_apply(procedure, args, env):
    """Apply procedure to args in env; ensure the result is not an Unevaluated."""
    validate_procedure(procedure)
    val = scheme_apply(procedure, args, env)
    if isinstance(val, Unevaluated):
        return scheme_eval(val.expr, val.env)
    else:
        return val

#如何做到尾递归？scheme_eval=opt(schema_eval)
#在tailcontext则返回uneva，跳过计算？何时计算？
#调用eval会检测是否为tailcontext，否则？？？，是则？？？
#正常来说，对于多层叠加的if等，需要先算一个operand再返回
#此时将operand作为uneva返回，在上一层计算
#如果一个uneva出现在tailcontext上，就会继续向上传递
#第一个调用肯定不是tailcontext，看后续调用是不是tailcontext
#注意非tailcontext内部一定不是tailcontext，如何实现？
#不用实现，内部继续走uneva，外部不走并产生空间调用
#那些是tailcontext？if cond define（lambda） 有方法论，要逐一检验所有函数？
def optimize_tail_calls(unoptimized_scheme_eval):
    """Return a properly tail recursive version of an eval function."""
    def optimized_eval(expr, env, tail=False):
        """Evaluate Scheme expression EXPR in Frame ENV. If TAIL,
        return an Unevaluated containing an expression for further evaluation.
        """
        if tail and not scheme_symbolp(expr) and not self_evaluating(expr):
            return Unevaluated(expr, env)

        result = Unevaluated(expr, env)
        # BEGIN OPTIONAL PROBLEM 3
        while isinstance(result,Unevaluated):
            result=unoptimized_scheme_eval(result.expr,result.env)
        return result
        # END OPTIONAL PROBLEM 3
    return optimized_eval






################################################################
# Uncomment the following line to apply tail call optimization #
################################################################

scheme_eval = optimize_tail_calls(scheme_eval)
