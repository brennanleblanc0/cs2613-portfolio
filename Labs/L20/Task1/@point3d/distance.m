function retval = distance(p, other)
  retval = sqrt(distance(p.point2d, other.point2d)^2 + (other.z - p.z)^2);
endfunction
