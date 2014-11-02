 x = [-2:0.01:10];
 y = 3*x.^3-26*x+6;
 deriv1 = 9*x.^2-26;
 deriv2 = 18*x;
 plot(x, y, '-b')
 hold on
 plot(x, deriv1, '--r')
 plot(x, deriv2, ':k')
 hold off
 
 