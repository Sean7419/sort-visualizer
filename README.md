# sort-visualizer

This program uses Tkinter to setup a GUI to allow a user to generate and select variables for the sorting algorithm visualization

CURRENT PROGRESS
  - Bubble Sort: Written 08/26/21 @10:00 and visualized 08/26/21 @17:00
  - Merge Sort: Written 08/26/21 @10:30 and visualized 08/26/21 @17:30
  - GUI with Tkinter: Written 08/26/21 @13:00

KNOWN BUGS:
  - Buttons are not supplying feedback when pressed and do not appear a different color
  - Merge Sort visualization runs slow on some machines
    - If the program runs slow on your machine, changing the time.sleep() within the merge_sort() function to a float litteral fixes the problem
    - Permanent fix is IN PROGRESS

FUTURE UPDATES:
  - Bug fixes: IN PROGRESS
  - More Algorithms: IN PROGRESS
  - Better representation for merge sort: TO DO
    - Intend on a new GUI to better visualize all sorts
    - Intend to break up canvas into two, one shows overall sorting, other shows what elements are being sorted
