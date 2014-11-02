function [ contributions, requirements, rhs ] = getKnapsackInfo(daModelFile)
daData = load(daModelFile);
contributions = daData(2:end, 2);
requirements = daData(2:end, 3);
rhs = daData(1,2);
end

