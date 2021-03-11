library("neuralnet");

X = matrix(c(-0.9,  0.75,
             -0.8,  0.7,
             -0.7,  0.65,
              0.5,  0.5,
              0.3,  0.3,
              0.2,  0.2,
              0.9, -0.7,
              0.95,-0.8,
              0.7, -0.9,
              0.7,  0.9,
              0.85, 0.75,
              0.8,  0.7,
             -0.3, -0.3,
             -0.4, -0.45,
             -0.5, -0.5,
             -0.8, -0.8,
             -0.7, -0.85,
             -0.7, -0.9), nrow = 18, ncol = 2, byrow = T);

d = matrix(c(1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0), nrow = 18);

train_set = as.data.frame(cbind(X,d))
colnames(train_set) = c("x1", "x2", "d")

rm(X, d)
attach(train_set)

nn = neuralnet(d ~ x1 + x2, data=train_set,  hidden=c(4,3), threshold = 0.001)
#plot(nn)

test_set = data.frame(x=0, y = 0);
cont = 0;
for (i in seq(-1,1, by=0.05)) {
  for (j in seq(-1,1, by=0.05)) {
    cont = cont+1;
    test_set[cont, 1:2] = c(i,j)
  }
}

color = compute(nn, test_set)
color = color$net.result > 0.5
color = as.numeric(color) +4

plot(test_set, col=color, pch=color-1)
for (i in 1:4) {
  points(train_set[1:18,1:2], col=d+2, pch=d+1)
}

detach(train_set)



