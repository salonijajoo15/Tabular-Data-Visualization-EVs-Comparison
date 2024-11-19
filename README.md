# Tabular Data Visualization: EVs Comparison

This repository contains a project focused on **tabular data visualization** to compare **Electric Vehicles (EVs)** based on various attributes. The aim is to provide an interactive and visually appealing way to analyze and compare EV models, using tools like Python, Pandas, and Matplotlib.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Data](#data)
- [Installation](#installation)

## Introduction

Electric Vehicles (EVs) are gaining popularity due to their eco-friendliness and efficiency. This project aims to visualize EV data in a tabular format, highlighting key attributes such as range, battery capacity, charging speed, and more. The visualization allows users to easily compare models and gain insights into the EV market.

## Features

- **Data Cleaning**: Prepares raw EV data for visualization.
- **Interactive Tables**: Displays EV attributes in a clean, user-friendly format.
- **Custom Visualizations**: Creates bar charts, scatter plots, and other visual aids to enhance understanding.
- **Sorting and Filtering**: Enables users to filter data based on specific criteria (e.g., price range, range per charge).

## Data

The dataset includes key attributes of EV models such as:

- Manufacturer
- Model
- Range (in miles or kilometers)
- Battery Capacity (kWh)
- Charging Time
- Price
- Other relevant specifications

## PREREQUISITES

Python 3.11 or higher

Required Libraries:
- pandas - 2.2.2
- seaborn - 0.13.2
- matplotlib - 3.9.2
- argparse - 1.1

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/salonijajoo15/Tabular-Data-Visualization-EVs-Comparison.git
   cd Tabular-Data-Visualization-EVs-Comparison
## Tasks and APIs

This project utilizes APIs to accomplish specific tasks for real-time and accurate EV data visualization. Below is a breakdown of the tasks, associated APIs, and their objectives:

### Task 1: Fetch EV Specifications
- **API Used**:
  ```bash
  python p1_bars.py -i <filename>
- **Example API Call**:
  ```bash
  python p1_bars.py -i evs_assignment1.xlsx

### Task 2: Fetch Real-Time Pricing Data
- **API Used**: 
  ```bash
  python p1_bubbles.py -i <filename> -x <attribute> -y <attribute> -c <attribute> -s <attribute>
- **Example API Call**:
  ```bash
  python p1_bubbles.py -i evs_assignment1.xlsx -x "Weight" -y "Range" -c "Top Speed" -s "Acceleration"

### Task 3: Retrieve Nearby Charging Station Data
- **API Used**: 
  ```bash
  python p1_splom.py -i <filename> -a <attribute1> <attribute2> <attribute3> <attribute4>
- **Example API Call**:
  ```bash
  python p1_splom.py -i evs_assignment1.xlsx -a Range Acceleration Efficiency Price



