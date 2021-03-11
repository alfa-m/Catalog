library("neuralnet")

# CLASSIFICATION

train_set = read.table("./data/amerindio_train.txt", header = T, sep = ";", stringsAsFactors = F)
test_set = read.table("./data/amerindio_teste.txt", header = T, sep = ";", stringsAsFactors = F)

nms = names(train_set)
form = as.formula( paste(" N1 + N2+ N3 + N4 ~ ", paste(nms[!(nms %in% c("N1", "N2", "N3", "N4"))], collapse = " + ")) )

nn = neuralnet(form, data=train_set, hidden = c(10), linear.output = F)

print(" ")
print(nn$result.matrix[1:3,])
print(" ")

out = compute(nn, test_set[, 1:202])

res = data.frame(round(out$net.result, 2))
res$MaxCol = max.col(res[1:4])
res$Output = paste("N", res$MaxCol, sep='')
res$TestVal = max.col(test_set[,203:206])
res$Answer = paste("N", res$TestVal, sep='')
res$Error = abs(res$MaxCol - res$TestVal)
colnames(res)[1:4] = c("N1", "N2", "N3", 'N4')

print(" ")
print("Number of Errors:")
print(sum(res$Error != 0))
print(" ")
print(res)
print(" ")

plot(res$TestVal, col='green', lwd=3, pch=20, ylim=c(0.5, 4.5), ylab= "Categories")
par(new=T)
plot(res$MaxCol, col='red', lwd=0.7, pch=20, ylim=c(0.5, 4.5), ylab= "Categories")

legend("bottomleft", inset=0.05, legend = c("Answer", "Net Output"), lty=0, pch=20, col=c('green', 'red'), lwd=c(3, 0.7))












