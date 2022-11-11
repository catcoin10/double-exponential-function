# double-exponential-function

This is a program designed to use the double exponential function (10^10^x) as a more precise form of scientific notation. Not only can it display more numbers, it can also go higher in terms of numbers stored (though that is not the point of this program).

I have an introduction to double exponential function: inputting 0 gets you to 10, 1 gets you to ten billion, and 2 gets you to a googol (a number larger than anything you can imagine in real life), and so on. In case you're curious about negative numbers, -1 gets you approximately five-fourths. But negative numbers are not implemented (though I could implement them later on, it wouldn't be too hard.

In order to make this anything useful, we need to get smaller. I decided not to go crazy small, and go down to the thousandths place. In addition, to make the program more flexible, I decided to add a multiplier function meaning that we multiply the output of the double exponential function by a certain number before converting it to an integer. This allows us to reach higher levels of precision. Inevitably, there are going to be some numbers that get "missed" by this model, especially as we get into bigger and bigger numbers.

It wasn't too hard to develop this program with Python but it did take some work and thinking I like to reserve for a math class. I decided to do this because I was thinking about this idea for a while and it's interesting to see it actually get implemented on the computer.

In order to run the program and save it to a file, type "python3 -u scinotation.py>results.txt" (without quotes) and make sure your directory can write to the file results.txt. You can also check what a number would give you by typing python3 sci-notation-check.py exponent multiplier.
