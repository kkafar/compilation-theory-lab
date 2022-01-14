a = 10;
b = 11;

if (a < b) {
  print "Deklaracja zmiennej w if'ie";
  c = 10;
  print c;
}

print "Zmienna poza if'em";
print c;


while (a < b) {
  print "Deklaracja zmienniej w petli while";
  d = 10;
  print "Zmienna w petli";
  print d;
  a += 1;
}

print "Zmienna poza petla";
print d;

for x = 1:1 {
  print "Deklaracja zmiennej w petli for";
  e = 10;
  print "Zmienna w petli";
  print e;
}

print "Zmienna poza petla";
print e;

if (a == b) {
  print "Deklaracja w if'ie";
  f = 10;
  print f;
  if (a == b) {
    print "Deklaracja w zagniezdzonym if'ie";
    g = 10; 
    print g;
  }
  print "Wartosci w if'ie";
  print f;
  print g;
}

print "Wartosci poza if'em";
print f;
print g;
