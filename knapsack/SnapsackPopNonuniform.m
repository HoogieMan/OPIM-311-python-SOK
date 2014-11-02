function [daPop] = SnapsackPopNonuniform (m, n, ps, pf)
probs = linspace(ps, pf, m);
daPop = rand(m,n);
for ii = 1:m
    daPop(ii,:) = daPop(ii,:) <= probs(ii);
end
end
