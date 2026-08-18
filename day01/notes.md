## Relearning Python properly (ish)

- python isn't just a language, its also a program thats an interpreter, hehe
- functions: action that lets one do something in program (some are predetermined e.g. `print()`)
- argument is the input to a function that affects its behaviour
- function -> side effect

- `print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)`
    - `*objetct` the print fn can take any number of objects
    -  `sep=" "` basically. when you call multiple obijecsts in the `print()` fn, it automatically spacs them out cos of the `sep` arg

---

## DSA (BIG"O" NOTATION) using [Boot Dev](https://www.boot.dev/lessons/555312c5-f6c7-497f-b445-32cb12e728d2)
It is a characterization of algorithms according to their worst case growth rates: basically, how slow or fast an algorithm becomes as the input increases.
- **O(1):** Constant time, this algorithm gives its output at the same time no matter the amount of inputs. The simple explanation for this is because the function or whatever is being called to perform the algorithm is preloaded in memory, so it takes as much time as it would for 1, for 2, for 1000 values, e.g. the `len()` function, called on a list with 10 values will run at the same time it takes for a list with 100 values 
- **O(n):** Big "O" characterization of order of n, i.e it is linearly proportional, the amount of time it tales to run the algiorithm is linearly proportional to the input size, e.g. a for loops that iterates over a list of 10 values will take 10 iterations, but if the list has 100 values, it will take 100 iterations, and so on
- **O(n^2):** e.g. a for loop in a for loop as the input gets big, the time it takes to run the algorithm increases exponentially, e.g. a nested for loop that iterates over a list of 10 values will take 100 iterations, but if the list has 100 values, it will take 10,000 iterations, and so on
- **O(log(n)):** e.g. the binary search algorithm, which is a search algorithm that finds the position of a target value within a sorted array. It works by repeatedly dividing in half the portion of the list that could contain the target value, until you've narrowed down the possible locations to just one. the time complexity of the binary search algorithm is O(log(n)) because with each iteration, the size of the input is halved, leading to a logarithmic growth rate. This means that as the input size increases, the time it takes to run the algorithm increases at a much slower rate compared to linear or quadratic algorithms