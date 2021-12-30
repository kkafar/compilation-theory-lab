A = eye(3);
print 'A', A;
B = ones(3);
print 'B', B;
C = A .+ B;
print 'C', C;

D = zeros(3, 4);
print 'D', D;
D[0, 0] = 42;
#D[1:3, 2:4] = 7;
print D;
print D[0, 0];
