import time

def bubble_sort(data, display_data, time_delay):
    """
    Bubble sort algorithm

    :param data: List of data being sorted
    :param display_data: function that displays the data
    :param time_delay: amount of time delay
    :return: None
    """
    for _ in range(len(data)-1):
        for i in range(len(data)-1):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                display_data(data, ['green' if x == i or x == i+1 else 'red' for x in range(len(data))])
                time.sleep(time_delay)
    display_data(data, ['green' for x in range(len(data))])

def merge_sort(data, display_data, time_delay):
    """
    Merge Sort algorithm
    for this function the colors indicated are
    blue: breaking down sub sets
    yellow: sets being sorted
    green: the sorted set/sub sets

    :param data: list of data being sorted
    :param display_data: function to display data
    :param time_delay: amount of time to delay
    :return: None
    """
    def merge(s1, s2):
        """
        Merge helper function

        :param s1: subset 1/Left (sorted)
        :param s2: subset 2/Right (sorted)
        :return: None
        """
        # Display what is being sorted/merged
        display_data(s1 + s2, ['yellow' for x in range(len(data))])
        time.sleep(time_delay)
        i = j = 0
        # Swap data with the smallest subset data point
        while i + j < len(data):
            if j == len(s2) or (i < len(s1) and s1[i] <= s2[j]):
                # Left had smaller data
                data[i+j] = s1[i]
                i += 1
            else:
                # Right had smaller data
                data[i+j] = s2[j]
                j += 1
        # Display new merged/sorted data
        display_data(data, ['green' for x in range(len(data))])
        time.sleep(time_delay)

    # Ends recursion
    if len(data) < 2:
        return

    # Display the sub set
    display_data(data, ['blue' for x in range(len(data))])
    time.sleep(time_delay)

    # Determine middle and get two subsets (left/right)
    mid = len(data)//2
    sub1 = data[0:mid]
    sub2 = data[mid:len(data)]

    # Call merge_sort with new subsets
    merge_sort(sub1, display_data, 1)
    merge_sort(sub2, display_data, 11)
    merge(sub1, sub2)
    display_data(data, ['green' for x in range(len(data))])

def insertion_sort(data, display_data, time_delay):
    """
    Insertion sort algorithm

    :param data: list of data points being sorted
    :param display_data: function to display data
    :param time_delay: time delay
    :return: None
    """
    for j in range(1, len(data)):
        i = j
        while i > 0 and data[i] <= data[i-1]:
            data[i], data[i-1] = data[i-1], data[i]
            i -= 1
