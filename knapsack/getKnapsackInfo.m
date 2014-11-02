%%%%% Exercise 1 %%%%%%%%%%%
function [ contributions, requirements, rhs ] = getKnapsackInfo(daFile)
daData = load(daFile);
contributions = daData(2:end, 2);
requirements = daData(2:end, 3);
rhs = daData(1,2);
end

