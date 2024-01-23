garbage = 0;
function result = unitVector(v)
  if (all(v) == 0 )
    result = v;
  elseif
    mag = sqrt(dot(v,v));
    result = v / mag;
  endif
endfunction
