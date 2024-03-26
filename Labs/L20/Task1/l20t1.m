p1 = point2d([1,2]);
p2 = point2d([3,-4]);
disp("p1");
disp(p1);
disp("p2");
disp(p2);
disp("Now setting p1.y");
get(p1, "y")
p1 = set(p1, {"y", 3});
get(p1, "y")
disp("Distance");
distance(p1,p2)
disp("Now, 3 3D points");
p3 = point3d({p1,5});
p4 = point3d({p2,-6});
p5 = point3d({3,3,3});
disp("Setting p3.z");
get(p3, "z")
p3 = set(p3, {"z", 6});
get(p3, "z")
disp("Setting p3.y");
get(p3, "y")
p3 = set(p3, {"y", 1});
get(p3, "y")
disp("Perimeter of a triangle");
triangle(p3, p4, p5)

