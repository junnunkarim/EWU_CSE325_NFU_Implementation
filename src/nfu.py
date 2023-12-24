import random
import time

NUM_PAGES = 16
NUM_FRAMES = 8
REFERENCE_COUNTER = 8


def page_shift_ref_bit(page_index, page_ref_counter_list, value):
    # shift bits to the right
    page_ref_counter_list[page_index] = [value] + page_ref_counter_list[page_index][:-1]


def page_ref_count(frame_list, page_ref_counter_list, page_ref_count_list):
    for i in range(len(frame_list)):
        page_index = frame_list[i]

        if page_index != -1 and (1 in page_ref_counter_list[page_index]):
            index_of_first_1 = page_ref_counter_list[page_index].index(1)
            count = page_ref_counter_list[page_index][:index_of_first_1].count(0)

            page_ref_count_list[page_index] = count
        else:
            count = 8

            page_ref_count_list[page_index] = count


def page_fault(
    insert_page_index,
    page_ref_counter_list,
    page_ref_count_list,
    frame_list,
    output_file,
):
    max = page_ref_count_list[frame_list[0]]
    index = 0

    for i in frame_list:
        if i != -1 and i < NUM_FRAMES and page_ref_count_list[frame_list[i]] > max:
            max = page_ref_count_list[frame_list[i]]
            index = i

    # find the page to remove
    remove_page_index = index

    # delete reference counter and count of the removed page
    page_ref_counter_list[remove_page_index] = [0] * REFERENCE_COUNTER
    page_ref_count_list[remove_page_index] = 0

    print(
        f"Removed page {frame_list[remove_page_index]} and inserted page {insert_page_index} in frame {remove_page_index}",
        file=output_file,
    )

    frame_list[remove_page_index] = insert_page_index


def main(output_file):
    page_list = [0] * NUM_PAGES
    page_ref_counter_list = [[0] * REFERENCE_COUNTER for _ in range(NUM_PAGES)]
    # for finding the page to remove from frame
    page_ref_count_list = [0] * NUM_PAGES

    # holds page indexs
    # -1 means not holding any page index
    frame_list = [-1] * NUM_FRAMES

    clock_tick = 0
    replace_count = 0

    old_page_list = page_list.copy()

    print(f"number of pages: {NUM_PAGES}", file=output_file)
    print(f"number of page frames: {NUM_FRAMES}", file=output_file)
    print(file=output_file)

    while True:
        for _ in range(16):
            # generate a random count of 1s (highest count 8)
            count_of_ones = random.randint(0, 8)

            # generate a list with the specified count of 1s and remaining 0s
            page_list = [1] * count_of_ones + [0] * (16 - count_of_ones)

            # shuffle the sublist to randomize the order
            random.shuffle(page_list)

        print(f"clock_tick {clock_tick}", file=output_file)
        print(f"replace count {replace_count}", file=output_file)

        for i in range(NUM_PAGES):
            if clock_tick == 0:
                if page_list[i] == 1:
                    page_shift_ref_bit(i, page_ref_counter_list, 1)
                    page_ref_count(
                        frame_list, page_ref_counter_list, page_ref_count_list
                    )

                    if frame_list.count(-1) == 0:
                        page_fault(
                            i,
                            page_ref_counter_list,
                            page_ref_count_list,
                            frame_list,
                            output_file,
                        )
                        replace_count += 1
                    else:
                        empty_index = frame_list.index(-1)
                        frame_list[empty_index] = i
                        print(
                            f"Inserted page {i} in frame {empty_index}",
                            file=output_file,
                        )
                        replace_count += 1

            elif old_page_list[i] == page_list[i]:
                if page_list[i] == 1:
                    page_shift_ref_bit(i, page_ref_counter_list, 1)
                    page_ref_count(
                        frame_list, page_ref_counter_list, page_ref_count_list
                    )

                    if frame_list.count(-1) == 0:
                        page_fault(
                            i,
                            page_ref_counter_list,
                            page_ref_count_list,
                            frame_list,
                            output_file,
                        )
                        replace_count += 1
                    else:
                        empty_index = frame_list.index(-1)
                        frame_list[empty_index] = i
                        print(
                            f"Inserted page {i} in frame {empty_index}",
                            file=output_file,
                        )
                        replace_count += 1

            elif old_page_list[i] != page_list[i]:
                page_shift_ref_bit(i, page_ref_counter_list, 0)
                page_ref_count(frame_list, page_ref_counter_list, page_ref_count_list)

            time.sleep(0.001)

        old_page_list = page_list.copy()
        clock_tick += 1

        print(f"page table: {page_list}", file=output_file)
        print(f"frame containing pages: {frame_list}", file=output_file)
        print(file=output_file)


if __name__ == "__main__":
    with open("output.txt", "w") as output_file:
        main(output_file)
