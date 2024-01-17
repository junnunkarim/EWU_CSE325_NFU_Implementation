# CSE325 Project - NFU Page Replacement Algorithm implementation

- University: East West University
- Course: CSE325 Operating Systems

# Directory Structure

```
.
├── README.md
├── docs
└── src
    ├── nfu.py
    └── output.txt
```

# Output

<details>
<summary><b>click here</b></summary>

### First 3 clock ticks are shown

```

number of pages: 16
number of page frames: 8

clock_tick 0
replace count 0
Inserted page 0 in frame 0
Inserted page 3 in frame 1
Inserted page 4 in frame 2
Inserted page 7 in frame 3
Inserted page 8 in frame 4
Inserted page 10 in frame 5
page table: [1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0]
frame containing pages: [0, 3, 4, 7, 8, 10, -1, -1]

clock_tick 1
replace count 6
page table: [0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1]
frame containing pages: [0, 3, 4, 7, 8, 10, -1, -1]

clock_tick 2
replace count 6
Inserted page 11 in frame 6
Inserted page 13 in frame 7
Removed page 0 and inserted page 15 in frame 0
page table: [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1]
frame containing pages: [15, 3, 4, 7, 8, 10, 11, 13]

clock_tick 3
replace count 9
Removed page 7 and inserted page 4 in frame 3
Removed page 8 and inserted page 15 in frame 4
page table: [1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1]
frame containing pages: [15, 3, 4, 4, 15, 10, 11, 13]

```

</details>

# Credit

- [Junnun Mohamed Karim](https://www.github.com/junnunkarim)
