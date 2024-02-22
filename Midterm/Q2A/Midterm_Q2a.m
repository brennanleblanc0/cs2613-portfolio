disp("");
function retval = uniqueChar(phrase)
    retval = "";
    addTo = 1;
    for i = 1:length(phrase)
        for j = 1:length(retval)
            if (retval(j) == phrase(i))
                addTo = 0;
                break;
            elseif (j == length(retval))
                addTo = 1;
            endif
        endfor
        if (addTo == 1)
            retval = [retval phrase(i)];
        endif
    endfor
endfunction

disp(uniqueChar("This example is a test"));