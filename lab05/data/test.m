A = eye(3);
B = ones(3);
print 'A', A;
print 'B', B;
C = A .+ B;
print 'C', C;

A += B;
print 'A', A;

D = zeros(3, 4);
D[0, 0] = 42;
print D;
D[1:3, 2:4] = 7;
print D;
print D[0, 0];

v = [1, 2, 3];
v[1] = 4;
print v;
print v[1];

v[0:2] = 7;
print v;

n = 5;
A = ones(n);

for i = 1:n {
    print A[1-1:i, 0:i];
}
