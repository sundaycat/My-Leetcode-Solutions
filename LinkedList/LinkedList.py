from ListNode import ListNode

'''
key points:
    1. dummy node
    2. merge sort two list
    3. quick sort a list by reference
    4. selection sort a list by reference
'''

class LinkedList(object):

    def __init__(self, values):

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

    '''
    # using dictionary to keep track of the original index of each node.
    def merge_sort_help(self, start, end, dicts):

        if (end - start) == 1:
            # cutoff the linked list before sorting
            dicts[start].next = None
            return dicts[start]
        else:
            # applied dictionary {}
            mid = (start + end) // 2
            l_list = self.merge_sort_help(start, mid, dicts)     # [start, mid)
            r_list = self.merge_sort_help(mid, end, dicts)       # [mid, end)

        return self.merge_list(l_list, r_list)
    
    def merge_sort(self):
        # generate a dictionary for the current linkedlist
        dicts = {}
        cur, keys = self.head, 0
        while cur:
            dicts[keys] = cur
            cur = cur.next
            keys += 1

        return self.merge_sort_help(0, len(dicts), dicts)
    '''

    # 运用快慢指针，将快慢指针先指向头结点，快指针移动2个步长，慢指针移动1个步长，当快指针指向链表末尾的时候，慢指针刚好就在中间节点上。
    def find_middle(self, head):

        if not head or not head.next:
            return head

        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge_sort_helper(self, head):

        # base case, return the node itself when the list length is 1
        if not head or not head.next:
            return head

        # find the middle node by slow-fast pointer and cut off the list before sorting
        mid = self.find_middle(head)
        rhead = mid.next
        mid.next = None

        l_list = self.merge_sort_helper(head)
        r_list = self.merge_sort_helper(rhead)

        return self.merge_list(l_list, r_list)

    def merge_sort(self):
        return self.merge_sort_helper(self.head)

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

    # remove the node associated with target value, using recurrsion.
    def remove_target(self, head, target):
        if not head:
            return head

        if head.value == target:
            head = self.remove_target(head.next, target)
        else:
            head.next = self.remove_target(head.next, target)

        return head

    # Remove Duplicates from Sorted List 1
    def __remove_duplicate(self, head):
        if not head:
            return head

        cur = head
        # outer loop go through the whole linked list
        while cur:
            # using inner loop instead of if-else to handle multiple-duplicate case like: 1-1-1-None
            while cur.next and cur.next.value == cur.value:
                cur.next = cur.next.next
            cur = cur.next

    def remove_duplicate(self):
        self.__remove_duplicate(self.head)

    # 82. Remove Duplicates from Sorted List 2
    def __remove_duplicate_1(self, head):
        if not head:
            return head

        cur = dummy = ListNode(None)
        dummy.next = head
        while cur.next and cur.next.next:
            if cur.next.value == cur.next.next.value:
                cur_val = cur.next.value
                while cur.next and cur.next.value == cur_val:
                    cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy.next

    def remove_duplicate_1(self):
        self.head = self.__remove_duplicate_1(self.head)

    # O(n)
    def rotate_right(self, head, k):

        if not head or not head.next or k == 0:
            return head

        cur = head
        l = 0
        while cur:
            l += 1
            cur = cur.next

        # find the position of the head node after rotation
        if k % l == 0: return head
        pos = l - (k % l) + 1

        # find the new head node and its previous node and cut off the linkedlist
        pre = head
        while pos > 2:
            pre = pre.next
            pos -= 1
        new_head = pre.next
        pre.next = None

        # find the tail node of the second list
        tail = new_head
        while tail.next:
            tail = tail.next

        # merge two list together to form the rotated linkedlist
        tail.next = head
        head = new_head

        return head

    # recursion version
    def rotate_right_1(self, head, k):
        if not head or k == 0:
            return head

        # 每次递归时，先循环找出新链表的尾节点及它之前的节点
        pre = tail = head
        l = 1
        while tail.next:
            pre = tail
            tail = tail.next
            l += 1

        # 计算剩下的rotation次数
        k = k % l

        # make the rotation
        tail.next = head
        pre.next = None
        head = tail

        # 继续递归
        head = self.rotate_right_1(head, k - 1)

        return head

    def rotate_right_2(self, head, k):
        if not head or not head.next or k == 0:
            return head

        # find out the length of the list and its tail node
        l = 1, tail = head
        while tail.next:
            l += 1
            tail = tail.next

        # connect tail with head node to form a circle
        if k % l == 0: return head
        tail.next = head

        # calculate the position to cut off the circle to make the rotation
        pos = l - (k % l)
        new_tail = new_head = head
        while pos > 0:
            new_tail = new_head
            new_head = new_head.next
            pos -= 1
        new_tail.next = None
        head = new_head
        return head

'''    
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
list7.head = list7.merge_sort()
list7.print_list()

#list7.reverse(list7.head)
#list7.print_list()

values = [1]
list8 = LinkedList(values)
list8.print_list()
x = list8.find_middle()
print(x.value)


values = [5,6,8,6,3,2]
list1 = LinkedList(values)
list1.print_list()
list1.remove_target(list1.head, 6)
list1.print_list()
'''

values = [1,5,5,5]
list2 = LinkedList(values)
list2.print_list()
list2.remove_duplicate_1()
list2.print_list()

values = [1,2]
list3 = LinkedList(values)
#list3.reverse(list3.head)
list3.head = list3.rotate_right_2(list3.head, 2)
list3.print_list()