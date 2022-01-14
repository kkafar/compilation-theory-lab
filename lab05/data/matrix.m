A = eye(3);
B = ones(3);
C = A .+ B;
print C;

D = zeros(3, 4);
D[0, 0] = 42;
D[1:3, 2:4] = 7;
print D;
print D[0, 0];

E = D + 1;
print E;

V = [1, 2, 3];

print V[0];
print V[1:2];
print V[V[1:2]];

print D[0:1, 0:1];

D[0, 0] = 1;

print D[D[0:1, 0:1], 0];
