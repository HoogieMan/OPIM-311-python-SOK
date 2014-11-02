function [solution] = RandomTestSnapsackSoln( numDVars, prob1, daSeed )
rand('state',daSeed);
solution = rand(numDVars,1);
solution = solution <= prob1;
end
