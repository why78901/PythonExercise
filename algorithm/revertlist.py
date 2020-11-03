class ListNode(object):
	def __init__(self, val):
		super(ListNode, self).__init__()
		self.val = val
	nxt = None

def main():
	arr = [1, 2, 3, 4, 5]
	lst = []
	for item in arr:
		node = ListNode(item)
		if(len(lst) > 0):
			lst[len(lst) - 1].nxt = node
		lst.append(node)
	lst[len(lst) - 1].nxt = None
	head = revertlist(lst[0])
	while head is not None:
		print(head.val)
		head = head.nxt
		pass

def revertlist(head):
	if(head is None):
		return head
	result = ListNode(head.val)
	while(head.nxt is not None):
		head = head.nxt
		temp = ListNode(head.val)
		temp.nxt = result
		result = temp
	return result

if __name__ == '__main__':
    main();