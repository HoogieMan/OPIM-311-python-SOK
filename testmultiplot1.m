x = [-2:.1:4];
y = 3*x.^3 - 26*x + 10;
der1 = 9*x.^2-26;
der2 = 18*x;
plot(x,y,x,der1,x,der2)
