
a <- 1:5
b <- 46:50
rb <- rbind(a,b)

cb <- cbind(a,b)

setwd("F:\\R Course\\Datasets")
Orders <- read.csv("Orders.csv")
Ord_Details <- read.csv("Ord_Details.csv")

ord <- merge(Orders, Ord_Details,
             by = "Order.ID")

# OR
ord <- merge(Orders, Ord_Details,
             by.x = "Order.ID",
             by.y = "Order.ID")


Lab_Uric <- read.csv("Lab_Uric.csv")
Lab_Keto17 <- read.csv("Lab_Keto17.csv")

adlb <- merge(Lab_Uric,Lab_Keto17,by.x = c("PatientID","Lab_test_Date"),
                                  by.y = c("PID","Lab_test_Date") )

A <- read.csv("A.csv")
B <- read.csv("B.csv")

# Inner Join
AB <- merge(A,B,by="IdNum")

# Left Outer Join
AB <- merge(A,B,by="IdNum", all.x = TRUE,
                            all.y = FALSE)

# Right Outer Join
AB <- merge(A,B,by="IdNum",all.x = FALSE,
                           all.y = TRUE)

# Full Outer Join
AB <- merge(A,B,by="IdNum", all.x = TRUE,
                            all.y = TRUE)

