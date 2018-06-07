class ListNode(object):

    def __init__(self, value):
        self.next = None
        self.value = value

class LinkedList(object):

    def __init__(self, values: object) -> object:

        if len(values) > 0:
            value = values[0]
            self.node = ListNode(value)
            self.head = self.node
            for i in values[1:]:
                self.insert_nodes(i)
        else:

            return None

    def print_list(self):
        cur = self.head
        while cur != None:
            print(cur.value, end = ', ')
            cur = cur.next
        print()

    def print_start_end(self, start, end):
        while start is not end:
            print(start.value, end=', ')
            start = start.next
        print()

    def insert_nodes(self, value):
        tail = self.get_tail(self.head)
        tail.next = ListNode(value)

    # remove the nodes contained the target value.
    # the original linkedlist remain the same.
    def remove_nodes(self, head, target):

        dummy = ListNode(None)
        dummy.next = head

        # pre: use to remove the current node from the linked list
        # cur: use to determine whether or not the current node should be delete
        pre, cur = dummy, head
        while cur:
            if cur.value == target:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next

        return dummy.next

    def search_by_index(self, head, index):

        if head is None or index < 0:
            return None

        current, count = head, 0
        while current is not None:

            if count == index:
                return current

            current = current.next
            count += 1

        return None

    def search_by_value(self, head, value):

        if not head:
            return None

        current = head
        while head is not None:

            if current.value == value:
                return current

            current = current.next

        return None

    def get_tail(self, start):
        if start is None or start.next is None:
            return start

        current = start
        while current.next is not None:
            current = current.next

        return current

    # Sort a linked list via merge sort
    def merge_list(self, head1, head2):

        idx1, idx2 = head1, head2

        # use dummy node to avoid comparing head node at the very beginning
        dummy = ListNode(None)
        cur = dummy
        while idx1 and idx2:

            if idx1.value < idx2.value:
                cur.next = idx1
                idx1 = idx1.next
            else:
                cur.next = idx2
                idx2 = idx2.next

            cur = cur.next

        if idx1:
            cur.next = idx1

        if idx2:
            cur.next = idx2

        return dummy.next

    def merge_sort(self, start, end, dicts):

        if (end - start) == 1:
            # cutoff the linked list before sorting
            dicts[start].next = None
            return dicts[start]
        else:
            # applied dictionary {}
            mid = (start + end) // 2
            l_list = self.merge_sort(start, mid, dicts) #[start, mid)
            r_list = self.merge_sort(mid, end, dicts) #[mid, end)

        return self.merge_list(l_list, r_list)

    # selection sort linked list, swapping by nodes reference
    def selection_sort(self, head):
        # null return null, one node return the node itself.
        if not head or not head.next:
            return head

        # create a dummy node
        dummy = ListNode(None)
        dummy.next = head

        # initialize pointers
        pre_mini = pre_outer = dummy
        inner = mini = outer = dummy.next
        while outer:
            while inner.next:
                if inner.next.value < mini.value:
                    # assign mini to next inner node
                    mini = inner.next
                    pre_mini = inner

                inner = inner.next

            # swap positions of mini and outer
            self.swap(pre_outer, outer, pre_mini, mini)
            self.print_list(dummy.next)

            # update pointers: pre_outer, outer, pre_mini, mini, inner
            # outer might change after swapping, so use pre_outer to update pointers
            pre_outer = pre_mini = pre_outer.next
            outer = pre_outer.next
            inner, mini = outer, outer

        return dummy.next

    # quick sort linked list, swap by nodes reference
    def partition(self, start, end):

        dummy = ListNode(None)
        dummy.next = start

        # initialize pointers
        pre_i, i = dummy, start
        pre_j, j = start, start.next
        while j is not end:

            # if swap happens, set has_swap to True, otherwise set it to False
            has_swap = False
            if j.value < start.value:

                has_swap = self.swap(i, i.next, pre_j, j)

                # move pre_i, i forward
                pre_i = pre_i.next
                i = i.next

                if has_swap:
                    # reset point j after swapping, make it point to next node of pre_j again
                    j = pre_j.next

            # move pre_j, j forward if swapping doesn't occur
            if j is not end and not has_swap:
                pre_j = pre_j.next
                j = j.next

        # swapping the first node(stores the pivot) with the ith node.
        self.swap(dummy, start, pre_i, i)

        # reset start and i after swapping
        pivot = start
        start = i

        return start, pivot

    def quick_sort(self, start, end):

        if start is None:

            return start

        elif start is end:

            return start

        else:

            # partition the linked list
            start, pivot = self.partition(start, end)

            # sorting before and after the pivot position
            l_head = self.quick_sort(start, pivot)
            r_head = self.quick_sort(pivot.next, end)

            # re-connect pivot node to the head of right linked list
            pivot.next = r_head

        return l_head

    # return True if swap happens, otherwise return false
    def swap(self, pre_outer, outer, pre_mini, mini):

        # 1. mini itself is outer
        # 2. mini and outer is adjacent
        # 3. mini is somewhere else in the linked list
        if outer is mini:
            return False
        elif outer.next == mini:
            outer.next = mini.next
            mini.next = outer
            pre_outer.next = mini
        else:
            temp = mini.next
            pre_outer.next = mini
            mini.next = outer.next
            pre_mini.next = outer
            outer.next = temp

        return True

    def reverse(self, cur):

        if not cur or not cur.next:
            self.head = cur
            return

        self.reverse(cur.next)
        temp = cur.next
        temp.next = cur
        cur.next = None

        return


# [5,4,8,6,2,3] [3,4,1,2]
# test case for quick sort
values = [5,4,8,6,2,3]
list6 = LinkedList(values)

#list6.print_list()
#tail = list6.get_tail(list6.head)
#list6.head = list6.quick_sort(list6.head, tail.next)
#list6.print_list()

values = [5,4,6,8,2,3]
list7 = LinkedList(values)
list7.print_list()
list7.reverse(list7.head)
list7.print_list()