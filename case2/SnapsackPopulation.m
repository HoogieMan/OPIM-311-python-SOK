function [daPop] = SnapsackPopulation(m, n, p)
daPop = rand(m,n) <= p;
end