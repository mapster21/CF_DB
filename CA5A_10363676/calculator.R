# Scientific calculator using functions written in R.
# Select steps between the dashed lines and run in sequence:

# Step 1---------------------------------------------------------------------------------------------------

add <- function(x, y) {
  return(x + y)
}

subtract <- function(x, y) {
  return(x - y)
}

multiply <- function(x, y) {
  return(x * y)
}

divide <- function(x, y) {
  return(x / y)
}

square <- function(x) {
  return(x * x)
}

cube <- function(x) {
  return(x * x * x)
}

squarert <- function(x) {
  return(sqrt(x))
} 

cosine <- function(x) {
  return(cos(x))
} 

sine <- function(x) {
  return(sin(x))
} 

tangent <- function(x) {
  return(tan(x))
} 

# take input from the user
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Square")
print("6.Cube")
print("7.Squarert")
print("8.Cosine")
print("9.Sine")
print("10.Tangent")

choice = as.integer(readline(prompt="Enter choice[1/2/3/4/5/6/7/8/9/10]: "))

# Step 2--------------------------------------------------------------------------------------------------

num1 = as.integer(readline(prompt="Enter first number: "))


# For choices 5 - 10 inclusive skip step 3
# Step 3 -------------------------------------------------------------------------------------------------

num2 = as.integer(readline(prompt="Enter second number: "))

# Step 4 -------------------------------------------------------------------------------------------------

operator <- switch(choice,"+","-","*","/")
result <- switch(choice, add(num1, num2), subtract(num1, num2), multiply(num1, num2), divide(num1, num2), 
                 square(num1), cube(num1), sqrt(num1), cos(num1), sin(num1), tan(num1))

print(paste(num1, operator, num2, "=", result))

# End -----------------------------------------------------------------------------------------------------