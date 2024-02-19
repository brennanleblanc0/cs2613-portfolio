disp("");
function result = unitVector(v)
  if (v == 0)
    result = v;
  elseif
    mag = sqrt(dot(v,v));
    result = v / mag;
  endif
endfunction

iter = input("How many values would you like to input? ");
vIn = zeros(1, iter);
for i = 1:iter
  vIn(i) = input("");
endfor

disp(unitVector(vIn));

