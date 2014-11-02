function [ solution ] = RandomSnapsackSoln(numDVars, prob1 ) 
solution = rand(numDVars,1)
solution = solution <= prob1
end
