function val = get(p, prop)
  switch (prop)
    case "x"
      val = p.x;
    case "y"
      val = p.y;
    otherwise
      error('@point2d/get: invalid PROPERTY "%s"', prop);
  endswitch
endfunction

