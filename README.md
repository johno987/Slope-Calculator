# Slope and Level Calculation Tool

A Python script designed to help site engineers and surveyors accurately calculate drainage runs and landscaping levels/slopes.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [How It Works](#how-it-works)
- [Usage](#usage)
  - [Menu Options](#menu-options)
  - [Example Workflows](#example-workflows)
- [Script Details](#script-details)
  - [Key Variables and Functions](#key-variables-and-functions)
- [Dependencies](#dependencies)
- [License](#license)

---

## Overview

This script prompts users for data such as levels and distances, then computes:
- **Slopes** (expressed as a ratio `1:x` and a percentage).
- **New Levels** after applying a slope over a specified distance, in either an uphill or downhill direction.

It also tracks previously calculated values (like the last computed slope or last new level), which can be reused for subsequent calculations.

---

## Features

1. **Slope Calculation**  
   - Calculates the ratio and percentage slope between two levels given a distance.  
   - Handles zero gradients gracefully (reports an error if dividing by zero).

2. **New Level Determination**  
   - Given a starting level, a slope, and a distance, the script calculates a new level.  
   - User chooses whether the slope is uphill (+) or downhill (–).

3. **Reusability**  
   - Retains the last computed slope or level, offering the option to reuse them in the next calculation.

4. **Input Validation**  
   - Ensures numeric values are entered where required.  
   - Guides the user with prompts if data is invalid.

---

## How It Works

1. The script runs in a loop, presenting a menu to calculate:
   - A **slope** (`S`)  
   - A **new level** (`N`)  
   - **Exit** (`X`)

2. For slope calculations (`S`):
   - Prompts for two levels and the distance between them.  
   - Computes `slope = distance / level_difference`, presenting it as `1:x` and as a percentage.

3. For new level calculations (`N`):
   - Prompts for a starting level.  
   - Asks if the user wants to reuse the previously calculated slope or input a new one.  
   - Collects a distance, then asks if the slope is uphill (`+`) or downhill (`-`).  
   - Calculates and displays the updated level.

4. The script saves the most recently calculated slope and level, allowing reuse in later operations.

---

## Usage

### Menu Options

Upon running the script, you will see:

Enter S to calculate a slope or N for a new level. It is X to exit the app


- **S** or **s**  
  Launches the slope calculation process.
- **N** or **n**  
  Launches the new level calculation process.
- **X** or **x**  
  Exits the script.

### Example Workflows

#### Calculating a Slope
1. Type **S** and press Enter.  
2. Enter two levels (e.g., `85.2` and `83.7`).  
3. Enter the distance between these points (e.g., `30`).  
4. The script displays the slope in both `1:x` format and as a percentage.

#### Calculating a New Level
1. Type **N** and press Enter.  
2. Enter the starting level (e.g., `100.0`).  
3. When prompted for a slope, choose to reuse the last calculated slope (if available) by pressing **P**, or enter a new slope (e.g., `50`).  
4. Enter the distance (e.g., `25`).  
5. Choose **+** for uphill or **-** for downhill.  
6. The new level is then calculated and displayed.

---

## Script Details

### Key Variables and Functions

- **Global Variables**  
  - `levelCount`: Tracks the number of levels entered.  
  - `lastCalculatedSlope`: Stores the last computed slope.  
  - `isLastSlope`: Indicates if a valid slope has been calculated previously.  
  - `lastCalculatedLevel`: Stores the last computed level.  
  - `isLastLevel`: Indicates if a valid level has been calculated previously.

- **Functions**  
  1. `getLevelDifference(levelOne, levelTwo)`: Returns the absolute difference between two levels.  
  2. `getDistance()`: Prompts the user for a distance and validates numeric input.  
  3. `getLevels()`: Prompts the user for a level value.  
  4. `slopeCalc()`: Controls the flow for calculating a slope between two levels, retrieves user input, and calculates the slope as `distance / level_difference`.  
  5. `getSlope()`: Retrieves the slope from user input (either reuse last or enter new).  
  6. `getDirection()`: Asks the user if the slope is uphill (`+`) or downhill (`-`).  
  7. `newLevel()`: Uses a start level, slope, distance, and direction to compute a new level.  

---

## Dependencies

- **Python 3.x** (No external libraries required; standard library usage only.)

