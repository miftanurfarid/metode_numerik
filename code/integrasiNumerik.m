x = 1:0.3:2.8;
fx = 2*x + 2;
est_int_fx = (0.3 / 2) * ( fx(1) + 2*(sum(fx(2:5)) ) + fx(end))