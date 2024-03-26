function pout = set(p,vargin)
  pout = p;
  switch (vargin{1})
    case "x"
      pout.x = vargin{2};
    case "y"
      pout.y = vargin{2};
  endswitch

