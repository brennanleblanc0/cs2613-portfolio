function p = point3d(v)
  if (isa(v{1}, "point2d"))
    p.point2d = [];
    p.z = v{2};
    p = class(p, "point3d", v{1});
  else
    temp = point2d([v{1}, v{2}]);
    p.point2d = [];
    p.z = v{3};
    p = class(p, "point3d", temp);
  endif

endfunction
