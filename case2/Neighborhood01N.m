function [daNeighborhood] = Neighborhood01N(snapsackSoln, Naway)
%snapsackSoln = [0 0 0 0 0 1 1 1 1 1];
N = length(snapsackSoln);


%%%creating the neighborhood of snapsackSoln look-alikes%%%
for numRows = 1:nchoosek(N, Naway);
    daNeighborhood(numRows,:) = [snapsackSoln];
end;


%%%changing one random locus in each row%%%%
for daRow = 1:N;
    changedSoln = snapsackSoln;
    pickrandom = round((N-1)*rand+1);
    locus = snapsackSoln(pickrandom);
    if locus == 0;
        locus = 1;
    else locus = 0;
    end
    
    changedSoln(pickrandom) = locus;
    daNeighborhood(daRow,:) = [changedSoln];
end        

daNeighborhood;


%%%determining duplicate rows%%%
[uniqueHood,index] = unique(daNeighborhood, 'rows');
repeatRowindex = setdiff(1:size(daNeighborhood,1),index);

repeatRows = daNeighborhood(repeatRowindex,:);
sizeRepeatRows = size(repeatRows);
numRepeatRows = sizeRepeatRows(1);

while numRepeatRows;
    %%%RE-determining duplicate rows%%%
    [uniqueHood,index] = unique(daNeighborhood, 'rows');
    repeatRowindex = setdiff(1:size(daNeighborhood,1),index);

    repeatRows = daNeighborhood(repeatRowindex,:);
    sizeRepeatRows = size(repeatRows);
    numRepeatRows = sizeRepeatRows(1);
%%%permuting and including the duplicate rows%%%
    for ii = 1:numRepeatRows;
        p = randperm(N);
        PermedRow = intrlv(repeatRows(ii,:), p);
        daNeighborhood(repeatRowindex(ii),:) = PermedRow;
    end
end