function [daPop] = task3()
daModelFile = 'knapsack101.txt';

%%%% task 2 begins %%%%%
popSize = 50;
mRate = 0.01;
xoverRate = 0.6;
numGenerations = 1;
daPenalty = 0.1;

%%%% task 3 begins %%%%%
initialP1 = 0.5;

%%%% task 1 %%%%
[ps, rs, rhs] = getKnapsackInfo(daModelFile);

%%%% task 3 %%%%
daPop = SnapsackPopulation(popSize, length(ps), initialP1);

end