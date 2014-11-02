function [bestsofarZ, bestsofarSoln, numEvals] = SnapsackGreedyHillClimb(daModelFile, numStarts, daPenalty)

daModelFile = 'knapsack101.txt';
[ps, rs, rhs ] = getKnapsackInfo(daModelFile);

soln = [1 1 1 1 1 1 1 1 1 1]

numTries = 500;
popSize = 50;
%mRate = 0.01;
%xoverRate = 0.6;
%numGenerations = 500;
daPenalty = 0.1;

initialP1 = 0.5;

daPop = SnapsackPopulation(popSize, length(ps), initialP1);

bestsofarZ = -111.0;
bestsofarSoln = zeros(1, length(ps));

%%%using 1-bit away neighborhood%%%
daNeighborhood = Neighborhood01(snapsackSoln)

for gen = 1:numStart
    daFitnesses = EvalSnapsackPop(daPop, ps, rs, rhs, daPenalty);
    
    if bestsofarZ < max(daFitnesses)
        [bestsofarZ, daIndex] = max(daFitnesses);
        bestsofarSoln = daPop(daIndex,:);
        fprintf('bestsofarZ = %8.3f\n', bestsofarZ)
    end
    
    fprintf('At end of search, bestsofarZ = %8.3f\n', bestsofarZ)
    fprintf('and bestsofarSoln = %8.3f\n', bestsofarSoln)
    
end
%%% task 6 %%%
% handled by return values
end