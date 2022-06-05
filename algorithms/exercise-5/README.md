# Flood Fill Algorithm

- Create an initial canvas that looks like this.
```
[3, 2, 1, 1, 1, 1, 1, 1]
[1, 1, 1, 1, 1, 1, 0, 0]
[1, 0, 0, 1, 1, 0, 1, 1]
[1, 2, 2, 2, 2, 0, 1, 0]
[1, 1, 1, 2, 2, 0, 1, 0]
[1, 1, 1, 2, 2, 2, 2, 0]
[1, 1, 1, 1, 1, 2, 1, 1]
[1, 1, 1, 1, 1, 2, 2, 1]
```

- Position yourself on (4,4).
- Your current color will be 2. Replace that color with 3 in a way that you do not affect differently colored adjacent cells.
- Canvas after flood fill should look like this:
```
[3, 2, 1, 1, 1, 1, 1, 1]
[1, 1, 1, 1, 1, 1, 0, 0]
[1, 0, 0, 1, 1, 0, 1, 1]
[1, 3, 3, 3, 3, 0, 1, 0]
[1, 1, 1, 3, 3, 0, 1, 0]
[1, 1, 1, 3, 3, 3, 3, 0]
[1, 1, 1, 1, 1, 3, 1, 1]
[1, 1, 1, 1, 1, 3, 3, 1]
```