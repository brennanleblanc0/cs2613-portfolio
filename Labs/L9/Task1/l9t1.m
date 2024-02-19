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

