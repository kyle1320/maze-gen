Maze Generation
==============

Custom Maze Generation in Python
--------------

This is a Python implementation of a maze generation algorithm of my own design.

I also included a code-golfed version of the algorithm, because why not.

# The Algorithm

The `Maze` class implements the maze generation algorithm.

To create a maze, the constructor `Maze(width, height)` is used, where `width` and `height` specify the dimension of the maze, with each dimension corresponding to the number of possible intersections along the horizontal and vertical axes, respectively.

The `Maze` object keeps track of the following:

  * `visited`: a set of cells that have been previously visited. Each cell is only visited once.
  * `edge`: the "frontier": a set of cells that are adjacent to visited cells, but have not themselves been visited.
  * `path`: a set of indices indicating which cells have been joined together. These indices are of the form `(Ax + Bx, Ay + By)` where `Ax`, `Ay`, `Bx`, and `By` are the coordinates of the two cells, `A` and `B`, that have been joined. You might ask whether these values are unique. In fact, they are, due to the fact that only adjacent cells can be joined.

Now, the maze generation algorithm is as follows:
  * Select an origin cell (default is the cell at (0, 0)).
  * Add the origin cell to `visited` and add its neighbors to `edge`.
  * While there are cells in `edge`:
    * select a cell in `edge`, call it `n`, and and an adjacent cell from `visited`, call it `p`.
    * join `n` and `p` and move `n` from `edge` to `visited`.
    * add non-visited neighbors of `n` to `edge`.
    * iterate the following until `n` has no neighbors in `edge`, or stop by random chance:
      * set `p` = `n` and set `n` to a neighboring cell from `edge`.
      * join `n` and `p`, and move `n` from `edge` to `visited`
      * add non-visited neighbors of `n` to `edge`.

That's it! You can think of the algorithm as repeatedly growing "braches" out from existing branches, until the entire grid has been filled. The origin serves as the "seed" for the first branch.

We can now test whether two adjacent cells `A` and `B` have an open space between them (instead of a wall) by checking whether `(Ax + Bx, Ay + By)` is in `path`.