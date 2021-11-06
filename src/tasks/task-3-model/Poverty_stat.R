
#install.packages("randomForest")

library(randomForest)






###########################################################################


##########################################     Population under Poverty

###########################################################################


par(oma=c(3,3,3,3),mar=c(5,1,5,1),mfrow=c(1,1))

sp1=read.csv("Population_under_poverty.csv")
dim(sp1)
sp1=na.omit(sp1)



set.seed(88884)


diamRF=randomForest(percentage_of_population_in_poverty~.,ntree=3000, data=sp1, mtry=3)
diamRF

varImpPlot(diamRF, pch=1, col="black", cex=1, main = "Shannon_Index (Exp_Hbc)")






############## partial Plot

par(oma=c(3,3,3,3),mar=c(5,1,5,1),mfrow=c(1,2))

partialPlot(diamRF,sp1, median_household_income, "response", main="median_household_income")
partialPlot(diamRF,sp1, per_capita_income, "response", main="per_capita_income")











###########################################################################


##########################################   Population under 18 under Poverty

###########################################################################


par(oma=c(3,3,3,3),mar=c(5,1,5,1),mfrow=c(1,1))

sp1=read.csv("Population_under_18_poverty.csv")
dim(sp1)
sp1=na.omit(sp1)



set.seed(88884)


diamRF=randomForest(percentage_of_population_under_18_in_poverty~.,ntree=3000, data=sp1, mtry=3)
diamRF

varImpPlot(diamRF, pch=1, col="black", cex=1, main = "Shannon_Index (Exp_Hbc)")






############## partial Plot

par(oma=c(3,3,3,3),mar=c(5,1,5,1),mfrow=c(1,2))

partialPlot(diamRF,sp1, median_household_income, "response", main="median_household_income")
partialPlot(diamRF,sp1, per_capita_income, "response", main="per_capita_income")














