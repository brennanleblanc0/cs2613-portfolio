f1 = @(x) (x^2 / 3) - 5;
f2 = @(x) log10(x+1);
compareTo = @(x,y) x <= y;

function retval = compareListPositions(f1, f2, compareTo, values)
  retval = 0;
  for i = 2:length(values)
    if (compareTo(f1(values(i-1)), f2(values(i))))
      retval += 1;
    endif
  endfor
endfunction

disp(compareListPositions(f1,f2,compareTo,1:10));
