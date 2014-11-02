function [bestsofarZ, bestsofarSoln] = task5biii()
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
    %%%%task 5a%%%%
    daFitnesses = EvalSnapsackPop(daPop, ps, rs, rhs, daPenalty);
    
%%%task 5a1%%%%
    if bestsofarZ < max(daFitnesses)
        [bestsofarZ, daIndex] = max(daFitnesses);
        bestsofarSoln = daPop(daIndex,:);
        fprintf('bestsofarZ = %8.3f\n', bestsofarZ)
    end
    %%% task 5bi %%%%
    daNewPop = rankNSelection(daPop, daFitnesses, rankPerCent);
    
    %%%task 5bii%%%
    daNewPop = mutate01array(daNewPop, mRate);
    %%%task 5biii%%%
    for counter = 1:2:popSize
        if xoverRate < rand
            avector = daNewPop (counter,:);
            bvector = daNewPop(counter+1,:);
            [newa, newb] = singlepointcrossover(avector, bvector);
            daNewPop(counter,:) = newa;
            daNewPop(counter+1,:) = newb;
        end
    end
daPop = daNewPop;
end
%%% task 6 %%%
% handled by return values
end