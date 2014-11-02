function [ daFitness ] = SnapsackFitness (objval, slack, daPenalty)
if slack >= 0
    daFitness = objval
else
    daFitness = daPenalty * objval + slack
end
end