function val = get(p, prop)
  if (prop == "z")
    val = p.z;
  else
    val = get(p.point2d, prop);
  endif
endfunction
