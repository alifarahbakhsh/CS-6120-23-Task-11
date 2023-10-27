# CS-6120-23-Task-11
A very simple garbage collector for Bril. It works correctly for all benchmarks in the canonical `mem` benchmarks, except for one (you can see which one in the csv file).
I did not have time to investigate the issue.
In the CSV file, all the cases showing missing for the first run mean that their output did not contain the remaining heap, but the outputs of the garbage-collecting interpreter were correct.
To use the interpreter, you should copy the `brili-gc.ts` file in your Bril folder, and install it just like normal `brili.ts`.
