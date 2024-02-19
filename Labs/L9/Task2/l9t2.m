# CS2613: Lab 9
# Starter Code

disp("");
function result = countLetters(msg)
  msg = tolower(msg);
  v = zeros(1, 26);
  for i = 1:length(msg)
    if (isalpha(msg(i)))
      v(msg(i) - 96) += 1;
    endif
  endfor
  result = v;
endfunction

function retval = starterFunction()
	inputFile = fopen ("Input.txt", "r");
  	retval = {};
	while (!feof (inputFile))
		line = fgetl(inputFile);
    most_com = "";
    most_num = 0;
    v = countLetters(line);
    for i = 1:26
      if (v(i) > most_num)
        most_com = native2unicode(i + 96);
        most_num = v(i);
      endif
    endfor
	    if(length(retval) == 0)
		    retval(1, 1) = most_com;
		    retval(1, 2) = num2str(most_num);
		  else
			  retval(length(retval)+1, 1) = most_com;
		    retval(length(retval), 2) = num2str(most_num);
		end
	end
	retval(2, :) = [];
end

disp(starterFunction());

