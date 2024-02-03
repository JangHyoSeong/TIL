class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    
    # 처음에 root가 빈 상태로 초기화
    # 만약 root 노드를 입력해준다면, 입력가능
    def __init__(self, root=None):
        self.root = root


    # BST에 값 삽입
    def insert(self, value):
        while True:
            if value < self.root.value:
                if self.root.left is not None:
                    self.root = self.root.left
                else:
                    self.root.left = Node(value)
                    break

            else:
                if self.root.right is not None:
                    self.root = self.root.right
                else:
                    self.root.right = Node(value)
                    break


    # 노드 탐색
    # 트리에 찾는 값이 있다면 True, 없다면 False 반환
    def search(self, value):
        self.current_node = self.root
        while self.current_node:
            if self.current_node.value == value:
                return True
            elif self.current_node.value > value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right
        return False


    # 삭제
def delete(self, value):
        # 삭제할 노드가 있는지 검사하고 없으면 False리턴
        # 검사를 한 후에는 삭제할 노드가 current_node, 삭제할 노드의 부모 노드가 parent가 된다.
        is_search = False
        self.current_node = self.root
        self.parent = self.root
        while self.current_node:
            if self.current_node.value == value:
                is_search = True
                break
            elif value < self.current_node.value:
                self.parent = self.current_node
                self.current_node = self.current_node.left
            else:
                self.parent = self.current_node
                self.current_node = self.current_node.right
        if is_search == False:
            return False
		
        # 삭제할 노드가 자식 노드를 갖고 있지 않을 때
        if self.current_node.left == None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = None
            else:
                self.parent.right = None
        
        # 삭제할 노드가 자식 노드를 한 개 가지고 있을 때(왼쪽 자식 노드)
        if self.current_node.left != None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = self.current_node.left
            else:
                self.parent.right = self.current_node.left
        
        # 삭제할 노드가 자식 노드를 한 개 가지고 있을 때(오른쪽 자식 노드)
        if self.current_node.left == None and self.current_node.right != None:
            if value < self.parent.value:
                self.parent.left = self.current_node.right
            else:
                self.parent.right = self.current_node.right                

        # 삭제할 노드가 자식 노드를 두 개 가지고 있을 때
        if self.current_node.left != None and self.current_node.right != None:
            self.change_node = self.current_node.right
            self.change_node_parent = self.current_node.right
            while self.change_node.left != None:
                self.change_node_parent = self.change_node
                self.change_node = self.change_node.left
            if self.change_node.right != None:
                self.change_node_parent.left = self.change_node.right
            else:
                self.change_node_parent.left = None
                
            if value < self.parent.value:
                self.parent.left = self.change_node
                self.change_node.right = self.current_node.right
                self.change_node.left = self.current_node.left
            else:
                self.parent.right = self.change_node
                self.change_node.left = self.current_node.left
                self.change_node.right = self.current_node.right

        return True


    # 탐색 코드 추가해야함





bst = BST()
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)