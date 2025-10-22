function matrika = matfunkcija(n)
%UNTITLED7 Summary of this function goes here
%   Detailed explanation goes here
A1 = diag(1:n);
A2 = triu(4*ones(n),1);
poddiag1 = ones(n-1,1);
A3 = diag(poddiag1,-1);
poddiag2 = (-1)*ones(n-2,1);
A4 = diag(poddiag2, -2);
matrika = A1 + A2 + A3 + A4;
end
