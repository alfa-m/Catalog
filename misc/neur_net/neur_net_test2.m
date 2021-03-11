
%{

- Octave list installed packages:
>> pkg list

- Install on octave:
>> pkg install -forge nnet

- Install on different directory:
>> pkg prefix ~/.octave_packages/
>> pkg install -forge nnet

- Load and unload packages on octave's path:
>> pkg load nnet
>> pkg unload nnet

%}


%  input & output:
x = 0:0.4:10;
y = sin(x);

% input layer:
in_layer = [0 10]		% cell_1 lower and upper bound

% number of neurons on hidden and  output layers:
neur = [5, 1]

% output functions on hidden and output layers:
out_funcs = {'tansig', 'tansig'}

%{
	logsig:		sigmoid (logistic),   x -> [ 0; 1]
	tansig:		tang hiperbolic,      x -> [-1; 1]
%}

% training algorithm:
train_alg = 'traingda'

%{
	traingd:	gradient descendent
	traingdm:	gd with mommentum
	traingda:	gd with adaptative learning rate
	traingdx:	gd with alr & mommentum
%}

% neural network
% net = newff (in_layer, neur, out_funcs, train_alg);

%on octave
net = newff (in_layer, neur, out_funcs, 'trainlm', train_alg);


% learning rate:
%net.trainParam.lr = 0.01;

% min mean squar error:
net.trainParam.goal = 0.005;

% max number of epochs:
net.trainParam.epochs = 1000;

% mean square error sampling (?):
%net.trainParam.show = 100;


% initiate random weights (not on octave)
%net = init(net);

% train the neural network (on octave: substitute 'finite' for 'isfinite')
net = train(net, x, y);



% test data set:
x_ts = 0:0.02:10;

% test nn
o = sim (net, x2);






% net 2
neur2 = [10, 1]
net2 = newff (in_layer, neur2, out_funcs, 'trainlm', train_alg);
net2.trainParam.goal = 0.001;
net2.trainParam.epochs = 562;
net2 = train(net2, x, y);


% test nn
o2 = sim (net2, x_ts);






% net 3
neur3 = [100, 1]
net3 = newff (in_layer, neur3, out_funcs, 'trainlm', train_alg);
net3.trainParam.goal = 0.001;
net3.trainParam.epochs = 179;
net3 = train(net3, x, y);


% test nn
o3 = sim (net3, x_ts);

% ploting results
plot(x,y, '+b');
hold on
plot(x_ts, o, 'm');
plot(x_ts, o2, 'g');
plot(x_ts, o3, 'r');






