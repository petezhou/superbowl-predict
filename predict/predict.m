function p = predict(theta, X)

m = size(X, 1);
p = zeros(m, 1);


p = sigmoid(X * theta);

for i = 1:size(p),
    if p(i) >= 0.25
        p(i) = 1;
    else
        p(i) = 0;
    endif
  
endfor



end
