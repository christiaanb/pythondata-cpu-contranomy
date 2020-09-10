function [31:0] ContranomyCoreDirect;
input [29:0] v1;
begin
  ContranomyCoreDirect = {v1[29:0],2'b00};
end
endfunction

