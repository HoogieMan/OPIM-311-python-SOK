function [ ps, rs, rhs ] = task1()
daModelFile = 'knapsack101.txt';
[ps, rs, rhs ] = getKnapsackInfo(daModelFile);
end
