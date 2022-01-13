A = eye(3);
print -A[0, 0];

B = [0, 7];

A[0, 0] = 5;
while (A[0,0] > 0){
    A[0, B[0]] -= 1;
    print(A[0, B[0]]);
}

A[0, 0] = 5;

x = A[0, 0];

for i = 1:x {
    print i;
}

A[0, 1] = -3;
print A[1, 2] < 4;
print(A');