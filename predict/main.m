clear ; close all; clc
%% Load Data
data = load('data.txt');
X = data(:, [1, 2]); y = data(:, 3);
%  Setup the data matrix appropriately, and add ones for the intercept term
[m, n] = size(X);
X = [ones(m, 1) X];
initial_theta = zeros(n + 1, 1);
%  Set options for fminunc to find minumum cost function
options = optimset('GradObj', 'on', 'MaxIter', 5000);
[theta, cost] = fminunc(@(t)(costFunction(t, X, y)), initial_theta, options);

%PLOTTING
plotDecisionBoundary(theta, X, y);
hold on;
xlabel('Points scored')
ylabel('Points allowed')
legend('Won super bowl', 'Did not win')
hold off;

%Probability
prob = sigmoid([1 420 250] * theta);
fprintf(['Team: 420 points scored, 250 points allowed. ' ...
         'Probability of winning the Super Bowl %f\n'], prob);     
% Yes or no
p = predict(theta, [1 420 250]);
fprintf(['Will they win superbowl? %f\n'], p)











