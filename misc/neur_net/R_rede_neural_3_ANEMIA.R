library("neuralnet")
library("grid")
library("gridExtra")

th = 0.001

orig_dir = getwd()
setwd("~/Documents/ENG. COMPUTAÇÃO/7_inteligencia_comp/scripts/")

anemia_train = "./data/anemia_train.txt"
anemia_teste = "./data/anemia_teste.txt"

train_set = read.table(anemia_train, header=T, sep = ';', stringsAsFactors = F)
test_set = read.table(anemia_teste, header=T, sep = ';', stringsAsFactors = F)

nms = names(train_set)
form = as.formula(paste("resp ~", paste(nms[nms != "resp"], collapse = " + ")))

nn = neuralnet(form, data=train_set, hidden = c(50, 30, 50), linear.output = F, threshold=th)

res = compute(nn, test_set[,1:400])
res = as.data.frame(res$net.result)

res$testTrueVals = test_set$V401
colnames(res)[1] = "testOutput"
res$error = abs(res$testOutput - res$testTrueVals)
res$err_TrueVal = round(abs(res$error / res$testTrueVals), 3)
res$err_TrueVal[ res$err_TrueVal > 1 ] = " > 1 "


plot(res$testTrueVals, col="green", pch=20, ylim = c(0,1), ylab= "Output")
par(new=T)
plot(res$testOutput, col="red",  ylim = c(0,1), ylab= "Output")
legend(40, 0.6, legend= c("Test values","Net output"), title = paste("Threshold=", th), col = c("green", "red"), pch = c(20, 1) )
par(new=F)

"
tab = tableGrob(res[1:15,] )
t = data.frame('Threshold'= th)
t = tableGrob(t)

grid.newpage()
grid.arrange(tab, t, ncol=2)
"


setwd(orig_dir)


