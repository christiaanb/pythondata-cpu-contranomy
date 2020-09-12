function [31:0] ContranomyCoreMachineStateDirect;
input [29:0] v1;
begin
  ContranomyCoreMachineStateDirect = {v1[29:0]
                                     ,2'b00};
end
endfunction

