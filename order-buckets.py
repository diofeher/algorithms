import sys

# Quando achava q era um movimento por vez
def nested_loop(inp) -> int:
    lst = list(inp)

    N = len(lst)
    B = 0
    K = []
    # 1 - Calculate number of buckets and N -> O(N)
    for i, elem in enumerate(lst):
        if elem == "B":
            # 2 - Create K using the positions of Bs
            K.append(i)
            B += 1

    # 3 - Return invalid if there is no available space to order the buckets
    if B * 2 - 1 > N:
        return -1

    # 4 - Create the best value at i by:
    # Comparing the current position of the buckets and the expected position on the sliding window
    # O(N * K)
    best_value = sys.maxsize
    for i in range(N):
        cur_value = 0
        j = i
        for pos in K:
            # We're placing the buckets every two empty spaces, starting at i
            cur_value += abs(j - pos)
            j += 2
        best_value = min(best_value, cur_value)

    return best_value


def nested_loop2(inp) -> int:
    lst = list(inp)

    N = len(lst)
    B = 0
    K = []
    # 1 - Calculate number of buckets and N -> O(N)
    for i, elem in enumerate(lst):
        if elem == "B":
            # 2 - Create K using the positions of Bs
            K.append(i)
            B += 1

    # 3 - Return invalid if there is no available space to order the buckets
    if B * 2 - 1 > N:
        return -1

    # 4 - Create the best value at i by:
    # Comparing the current position of the buckets and the expected position on the sliding window
    # O(N * K)
    best_value = sys.maxsize
    for i in range(N):
        cur_value = 0
        j = i
        for pos in K:
            # We're placing the buckets every two empty spaces, starting at i
            if pos != j:
                cur_value += 1
            j += 2
        best_value = min(best_value, cur_value)

    print(best_value)
    return best_value

def intersection(inp):
    lst = list(inp)

    N = len(lst)

    initial_pos = set()
    B = 0
    # 1 - Create a set of buckets -> O(N)
    for i, elem in enumerate(lst):
        if elem == "B":
            initial_pos.add(i)
            B += 1
    
    # 2 - Return invalid if there is no available space to order the buckets -> O(1)
    if B * 2 - 1 > N:
        return -1
    
    # 3 - Test intersections
    # O(N^2)
    best_value = sys.maxsize
    for i in range(N):
        cur_pos = set()
        # Create a set with the desired positions -> O(B * N)
        # O(B) - for-loop, O(N) - worst-case adding to set
        for j in range(0, B):
            cur_pos.add(i + j * 2)
        
        # The maximum number of moves is the same number of buckets, since if you have available space, 
        # it's certain that you can order the buckets using one move per bucket.
        cur_value = B
        # Check if the initial position being checked is on the current "sliding window" positions
        # Worst case this operation is O(B). It cannot be O(N) in worst case complexity because if B == N, 
        # it's returned earlier as an invalid input.
        for initial in initial_pos:
            if initial in cur_pos:
                cur_value -= 1
        
        # print(initial_pos, cur_pos)
        # min is O(1)
        best_value = min(best_value, cur_value)
    
    return best_value



def sliding_window_sum(inp):
    lst = list(inp)

    N = len(lst)
    B = lst.count("B")
    
    # 2 - Return invalid if there is no available space to order the buckets -> O(1)
    if B * 2 - 1 > N:
        return -1
    
    best_value = B
    for i in range(N):
        cur_value = B
        for j in range(B):
            cur_pos = i + j * 2
            if cur_pos > N - 1:
                break
            if lst[cur_pos] == "B":
                cur_value -= 1
        best_value = min(best_value, cur_value)

    return best_value

def dp(inp):
    lst = list(inp)

    N = len(lst)
    B = lst.count("B")
    
    # 2 - Return invalid if there is no available space to order the buckets -> O(1)
    if B * 2 - 1 > N:
        return -1
    
    best_value = B
    # O(N) outer loop - O(B) inner loop
    for i in range(N):
        # The maximum size of moves to put in order is the same number of buckets available
        cur_value = B
        # Current sliding window
        for j in range(B):
            cur_pos = i + j * 2
            if cur_pos > N - 1:
                break
            # Count how many B are in the right position
            # A sliding window starts with a B then it's followed by a dot .
            # Index access is O(1)
            if lst[cur_pos] == "B":
                cur_value -= 1
        best_value = min(best_value, cur_value)

    return best_value


def dp_o_n_prints(inp):
    lst = list(inp)
    print("Input: ", lst)

    N = len(lst)
    B = lst.count("B")
    
    # 2 - Return invalid if there is no available space to order the buckets -> O(1)
    if B * 2 - 1 > N:
        return -1
    
    # Calculate first sliding window -> O(B)
    last_in_place = 0
    last_sliding_window_buckets = 0
    size_sliding_window = B * 2 - 1
    cur_buckets = 0
    print("Size of sliding window (B * 2 - 1):", size_sliding_window)
    for i in range(size_sliding_window):
        if lst[i] == "B":
            last_sliding_window_buckets += 1
            if i % 2 == 0:
                last_in_place += 1

    print("Total of Buckets:", B)
    print("Initial sliding window - O(B)")
    print(lst[0: size_sliding_window], "Buckets in sliding window:", last_sliding_window_buckets, "Buckets in place:", last_in_place)
    maximum_in_place = last_in_place
    # O(N)
    print("start to slide - O(N)")
    for i in range(1, N):
        cur_buckets = last_sliding_window_buckets
        # All the buckets in place on the last window are out of place,
        # but the buckets out of place, are now in place
        cur_in_place = cur_buckets - last_in_place

        end_sliding_window = i + size_sliding_window

        if end_sliding_window > N:
            # We're out of bounds here
            break

        # Now we check the previous item out the sliding window
        if lst[i - 1] == "B":
            cur_buckets -= 1
        # And we check the LAST item on the sliding window
        if lst[end_sliding_window - 1] == "B":
            cur_buckets += 1
            cur_in_place += 1

        print(lst[i:end_sliding_window], "Buckets in sliding window:", cur_buckets, "Buckets in place:", cur_in_place)
        last_sliding_window_buckets = cur_buckets
        last_in_place = cur_in_place

        maximum_in_place = max(maximum_in_place, cur_in_place)

    return B - maximum_in_place


def dp_o_n(inp):
    lst = list(inp)
    N = len(lst)
    B = lst.count("B")
    
    # 2 - Return invalid if there is no available space to order the buckets -> O(1)
    if B * 2 - 1 > N:
        return -1
    
    # Calculate first sliding window -> O(B)
    last_in_place = 0
    last_sliding_window_buckets = 0
    size_sliding_window = B * 2 - 1
    cur_buckets = 0
    for i in range(size_sliding_window):
        if lst[i] == "B":
            last_sliding_window_buckets += 1
            if i % 2 == 0:
                last_in_place += 1

    maximum_in_place = last_in_place
    for i in range(1, N):
        cur_buckets = last_sliding_window_buckets
        # All the buckets in place on the last window are out of place,
        # but the buckets out of place, are now in place
        cur_in_place = cur_buckets - last_in_place
        end_sliding_window = i + size_sliding_window

        if end_sliding_window > N:
            # We're out of bounds here
            break

        # Now we check the previous item out the sliding window
        if lst[i - 1] == "B":
            cur_buckets -= 1
        # And we check the LAST item on the sliding window
        if lst[end_sliding_window - 1] == "B":
            cur_buckets += 1
            cur_in_place += 1

        last_sliding_window_buckets = cur_buckets
        last_in_place = cur_in_place

        maximum_in_place = max(maximum_in_place, cur_in_place)

    return B - maximum_in_place

def calc_min_moves_bucket_order(inp):
    return dp_o_n_prints(inp)


assert calc_min_moves_bucket_order("BB") == -1
assert calc_min_moves_bucket_order("..BB.B..") == 1
assert calc_min_moves_bucket_order(".BB") == 1        # B.B
assert calc_min_moves_bucket_order("BB.") == 1        # B.B
assert calc_min_moves_bucket_order("B...B.B") == 1    # ..B.B.B
assert calc_min_moves_bucket_order("B.....BB") == 2 
assert calc_min_moves_bucket_order("BB....BB") == 2   # .B.B.B.B 
assert calc_min_moves_bucket_order("BB.....BB") == 2  # .B.B.B.B.
assert calc_min_moves_bucket_order("BB......BB") == 3 # ...B.B.B.B.
assert calc_min_moves_bucket_order("B.B...BB") == 1   # B.B.B.B.
assert calc_min_moves_bucket_order("BBBB....") == 2   # B.B.B.B.
assert calc_min_moves_bucket_order("BBB....") == 1    # B.B.B.B.
