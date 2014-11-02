function [daFitnesses] = task5a()
daModelFile = 'knapsack101.txt';

%%% task 2%%%%
popSize = 50;
mRate = 0.01;
xoverRate = 0.6;
numGenerations = 1;
daPenalty = 0.1;

%%%% task 3%%%%
initialP1 = 0.5;

%%%%task 1%%%%
[ps, rs, rhs ] = getKnapsackInfo(daModelFile);

%%%% task 3%%%%
daPop = SnapsackPopulation(popSize, length(ps), initialP1);

%%%%task 4%%%%
bestsofarZ = -111.0;
bestsofarSoln = zeros(1, length(ps));

%%%%task 5%%%%
for gen = 1:numGenerations
    daFitnesses = EvalSnapsackPop(daPop, ps, rs, rhs, daPenalty);
end
end
