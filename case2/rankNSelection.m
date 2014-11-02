function [daNewPopulation] = rankNSelection(daPopulation, daFitnesses, rankPerCent)
daSize = size(daPopulation);
popSize = daSize(1);
numDecisions = daSize(2);
daNewPopulation = zeros(popSize, numDecisions);
rankCount = round(popSize * rankPerCent);
[~, iy] = sort(daFitnesses, 'descend');
iy = iy(1:rankCount);
for iCount = 1:popSize
    daIndex = randi(rankCount);
    daRow = iy(daIndex);
    daNewPopulation(iCount,:) = daPopulation(daRow,:);
end
end
