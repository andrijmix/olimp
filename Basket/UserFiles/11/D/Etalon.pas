var
  a,i,c,d:real;
  b:real;
  begin
    read(a);
    b:=a/1000;
    c:=trunc(b);
    d:=frac(b);
    writeln(c,' ',round(d*1000));
  end.