# London Underground Shortest Path Finder

This piece of code calculates the shortest path and distance between London Underground stations using Dijkstra's algorithm, implemented with the help of the NetworkX Python library. The input data is sourced from the *tube_data.xls* file, which contains runtime information between various stations.

## Features

- **Shortest Path Calculation**: Uses Dijkstra’s algorithm to determine the shortest travel time between two stations during peak hours.
- **London Underground Data**: Processes data from *tube_data.xls* to build a graph representing station connections and running times.
- **Customizable**: Easily change the stations or adjust data inputs for other analyses.

## Requirements

- Python 3.x
- `networkx` library
- `pandas` library
- Excel file `tube_data.xls` with a `Runtime` sheet that contains the following columns:
  - `Station from (A)`
  - `Station to (B)`
  - `AM peak (0700-1000) Running Time (Mins)`


## Example

- Shortest distance between **South Kensington** and **Liverpool Street**:
    - Distance: X minutes
    - Path: South Kensington → Station 1 → Station 2 → Liverpool Street

