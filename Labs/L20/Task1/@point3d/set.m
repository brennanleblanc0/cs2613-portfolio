function pout = set(p, vargin)
  pout = p;
  if (vargin{1} == "z")
    pout.z = vargin{2};
  else
    pout.point2d = set(p.point2d, vargin);
  endif
endfunction
