a = 0;
b = 1;
while (b < 10) {
    print b;
    b += a;
    a = b - a;
}