Here I am using first data dictionary to get the occurent of all different numbers  using the for loop on the input list nums
where the number don't exist in data I am setting the count to 1
and that I am using sorted function to sort the elements based on the values
adn then using another for loop I am take the corresponding number with the top k most
and returning a result list with top k elements

The time complexity is less than or equal to O(nlogn).


Additional Comments:
We can also do O(n) complexity if we use a bucketing method where we can bucket the elements based on the value