class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:

    def __init__(self, root=None):
        self.root = root


    # 재귀적으로 삽입
    def insert(self, value):
        self.root = self._insert(self.root, value)

    
    def _insert(self, root, value):

        # 탐색을 모두 끝내고 더이상 자식이 없다면
        if root is None:
            return Node(value)
        
        # 크기를 비교하여 왼쪽 아니면 오른쪽으로 이동
        if value < root.value:
            root.left = self._insert(root.left, value)
        elif value >= root.value:
            root.right = self._insert(root.right, value)

        return root # 부모 노드에 대한 참조를 반환


    # 삭제 호출
    def delete(self, value):
        self.root = self._delete(self.root, value)


    # 재귀적으로 삭제 수행
    def _delete(self, root, value):

        if root is None:
            return root
        
        if value < root.value:
            root.left = self._delete(root.left, value)
        elif value > root.value:
            root.right = self._delete(root.right, value)

        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            # 삭제할 노드의 오른쪽 서브트리에서 최소값을 찾아 대체
            # 왼쪽에서 최대값을 찾아도 됨
            root.value = self._get_min_value(root.right)
            root.right = self._delete(root.right, root.value)

        return root
    
    def _get_min_value(self, root):
        # 최소값을 찾는 보조 함수
        while root.left is not None:
            root = root.left
        return root.value
    
    def search(self, value):
        # 탐색 연산
        return self._search(self.root, value)
    
    def _search(self, root, value):
        # 재귀적으로 탐색 수행

        # 찾는 값이 없거나 찾았다면 그 노드를 리턴
        if root is None or root.value == value:
            return root
        
        if value < root.value:
            return self._search(root.left, value)
        return self._search(root.right, value)
    

    def inorder(self):
        # 중위 순회
        # 왼쪽 서브트리를 먼저 방문한 후 현재노드를 방문하고, 오른쪽 서브트리를 방문함
        # 순회를 수행하면 정렬된 순서로 노드를 방문함
        result = []
        self._inorder(self.root, result)
        return result
    
    def _inorder(self, root, result):
        # 중위 순회의 보조 함수
        if root:
            self._inorder(root.left, result)
            result.append(root.value)
            self._inorder(root.right, result)

    def preorder(self):
        # 전위 순회
        # 현재 노드를 먼저 방문한 후, 왼쪽 서브트리를 방문하고 마지막으로 오른쪽 서브트리를 방문
        # 트리를 복제하는데 유용하게 사용될 수 있음
        result = []
        self._preorder(self.root, result)
        return result
    
    def _preorder(self, root, result):
        # 전위 순회의 보조함수
        if root:
            result.append(root.value)
            self._preorder(root.left, result)
            self._preorder(root.right, result)

    def postorder(self):
        # 후위 순회
        # 왼쪽 서브트리를 먼저 방문한 후, 오른쪽 서브트리를 방문하고 마지막으로 현재 노드를 방문
        # 리프 노드부터 시작하여 부모노드로 올라가는 방식으로 순회함
        result = []
        self._postorder(self.root, result)
        return result
    
    def _postorder(self, root, result):
        # 후위 순회의 보조함수
        if root:
            self._postorder(root.left, result)
            self._postorder(root.right, result)
            result.append(root.value)

# 테스트

bst = BST()
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)

print("Inorder 순회:", bst.inorder())
print("Preorder 순회:", bst.preorder())
print("Postorder 순회:", bst.postorder())

bst.delete(20)
print("20 삭제 후 Inorder 순회:", bst.inorder())

search_key = 30
result = bst.search(search_key)
if result:
    print(f"{search_key}를 찾았습니다.")
else:
    print(f"{search_key}를 찾을 수 없습니다.")