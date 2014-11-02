function [ popSize, mRate, xoverRate, numGenerations ] = task2()
daModelFile = 'knapsack101.txt';
popSize = 50;
mRate = 0.01;
xoverRate = 0.6;
numGenerations = 1;
daPenalty = 0.1;
[ps, rs, rhs] = getKnapsackInfo(daModelFile);
end