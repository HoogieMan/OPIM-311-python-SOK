function [ objval, lhsval, slack ] = SimpleKnapsackEval (soln, ps, ws, b)
objval = soln * ps;
lhsval = soln * ws;
slack = b - lhsval;
end