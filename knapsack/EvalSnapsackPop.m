function [daFitnesses] = EvalSnapsackPop (daPop, ps, ws, b, daPenalty)
dims = size(daPop);
numSolutions = dims(1);
daFitnesses = zeros(numSolutions,1);
for ii = 1:numSolutions
    [objval, ~, slack] = SimpleKnapsackEval (daPop(ii, :), ps, ws, b);
    daFitnesses(ii) = SnapsackFitness(objval, slack, daPenalty);
end
end
