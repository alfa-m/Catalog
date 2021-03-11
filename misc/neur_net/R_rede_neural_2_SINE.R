library("neuralnet")

x = seq(0, 10, by=0.5)
y = sin(x)

train_set = as.data.frame(cbind(x,y))

rm(x,y)
attach(train_set)

plot(x,y, pch=3, col="blue", ylim = c(-1.1, 1.1), lwd=4)

nn = neuralnet(y ~ x, data = train_set, hidden =c(5))

#plot(nn)

x_test = seq(0, 10, by=0.01)
y_test = compute(nn, as.data.frame(x_test))$net.result

par(new=T)
plot(x_test, y_test, col='red', type='l', ylim = c(-1.1, 1.1), lwd=3, xlab='x', ylab = 'y')

par(new=T)
plot(x_test, sin(x_test), col="green", type = 'l', ylim=c(-1.1,1.1), lwd=2, xlab='x', ylab = 'y')

legend(0,-0.3, legend = c("Train", "Test", "Sin"), col = c("blue", "red", 'green'), lty = c(0,1,1), lwd=c(4,3,2), pch=c(3,-1,-1))



#print(nn$result.matrix[1:3,])

detach(train_set)
